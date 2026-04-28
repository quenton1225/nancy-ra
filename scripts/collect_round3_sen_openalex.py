import csv
import datetime as dt
import json
import re
import urllib.parse
import urllib.request
from pathlib import Path

BASE_URL = "https://api.openalex.org/works"
ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
TODAY = dt.date.today().isoformat()

OUT_CSV = DOCS / "64_round3_sen_candidates_raw.csv"
OUT_LOG = DOCS / "64_round3_sen_collection_log.md"

SCHEMA = [
    "record_id",
    "bucket",
    "query_string",
    "title",
    "authors",
    "year",
    "venue",
    "publication_type",
    "doi",
    "source_url",
    "citation_count",
    "citation_date",
    "domain_sen",
    "domain_education",
    "domain_adaptive",
    "domain_ai_analytics",
    "domain_observable_signal",
    "study_type",
    "sample_size",
    "population_type",
    "input_signal",
    "ai_method",
    "prediction_target",
    "evaluation_metrics",
    "decision",
    "decision_reason",
    "notes",
]

GROUPS = [
    {
        "prefix": "R3SE",
        "bucket": "SEN+Education",
        "target": 35,
        "domains": (1, 1, 0, 0, 0),
        "queries": [
            "special educational needs students learning support higher education",
            "special education needs inclusive education learning outcomes",
            "SEN students education technology learning support",
            "SEND students inclusive education higher education",
            "students with special educational needs learning difficulties education",
        ],
    },
    {
        "prefix": "R3SA",
        "bucket": "SEN+Adaptive",
        "target": 35,
        "domains": (1, 1, 1, 1, 0),
        "queries": [
            "special educational needs adaptive learning system",
            "special educational needs artificial intelligence education",
            "SEN adaptive learning educational technology",
            "SEND learning analytics adaptive support students",
            "learning difficulties personalized learning system AI",
        ],
    },
    {
        "prefix": "R3SO",
        "bucket": "SEN+ObservableSignals",
        "target": 35,
        "domains": (1, 1, 0, 1, 1),
        "queries": [
            "special educational needs learning analytics prediction",
            "SEN students eye tracking learning",
            "students with special educational needs machine learning education",
            "learning disabilities eye tracking reading comprehension machine learning",
            "inclusive education learning analytics intervention",
        ],
    },
    {
        "prefix": "R3SB",
        "bucket": "BridgeTerms",
        "target": 25,
        "domains": (1, 1, 1, 1, 1),
        "queries": [
            "neurodiversity special educational needs education",
            "neurodivergent students special educational needs",
            "autism ADHD dyslexia special educational needs adaptive learning",
            "functional needs students adaptive learning eye tracking",
        ],
    },
]

SEN_KW = [
    "special educational need",
    "special education need",
    "sen",
    "send",
    "additional learning need",
    "learning difficult",
    "learning disab",
    "student with disab",
    "neurodiverg",
    "neurodivers",
    "autism",
    "adhd",
    "dyslex",
]

EDU_KW = [
    "education",
    "learning",
    "student",
    "classroom",
    "school",
    "higher education",
    "teaching",
    "pedagog",
    "inclusive education",
]

ADAPT_KW = [
    "adaptive",
    "personaliz",
    "intervention",
    "scaffold",
    "assistive technolog",
    "support",
    "accessibility",
    "intelligent tutoring",
]

AI_KW = [
    "artificial intelligence",
    "machine learning",
    "learning analytics",
    "educational data mining",
    "data mining",
    "prediction",
    "model",
    "algorithm",
]

SIGNAL_KW = [
    "eye tracking",
    "gaze",
    "webcam",
    "interaction log",
    "lms log",
    "behavioral signal",
    "cognitive load",
    "attention",
]


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "nancy-ra-sen-round3/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def clean_text(value: str):
    if not value:
        return ""
    return re.sub(r"\s+", " ", value).strip()


def inverted_index_to_text(inv_idx):
    if not inv_idx:
        return ""
    pos_to_word = {}
    for word, positions in inv_idx.items():
        for position in positions:
            pos_to_word[position] = word
    if not pos_to_word:
        return ""
    return clean_text(" ".join(pos_to_word.get(i, "") for i in range(max(pos_to_word) + 1)))


def has_any(text: str, keywords):
    lowered = (text or "").lower()
    return any(keyword in lowered for keyword in keywords)


def relevant(work, strict: bool):
    title = clean_text(work.get("title") or "")
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    blob = f"{title} {abstract}".lower()

    has_sen = has_any(blob, SEN_KW)
    has_edu = has_any(blob, EDU_KW)
    has_adapt = has_any(blob, ADAPT_KW)
    has_ai = has_any(blob, AI_KW)
    has_signal = has_any(blob, SIGNAL_KW)

    if strict:
        return has_sen and has_edu and (has_adapt or has_ai or has_signal)
    return has_edu and (has_sen or has_adapt or has_ai or has_signal)


def pub_type(work):
    work_type = (work.get("type") or "").lower()
    if work_type == "article":
        return "journal"
    if work_type in {"proceedings-article", "peer-review"}:
        return "conference"
    if work_type == "preprint":
        return "preprint"
    return "review_article" if "review" in (work.get("title") or "").lower() else work_type or "unknown"


def parse_doi(work):
    doi = work.get("doi") or ""
    if doi.startswith("https://doi.org/"):
        return doi.replace("https://doi.org/", "")
    return doi


def author_str(work):
    names = []
    for authorship in work.get("authorships", [])[:8]:
        name = ((authorship.get("author") or {}).get("display_name") or "").strip()
        if name:
            names.append(name)
    return "; ".join(names)


def venue(work):
    primary = work.get("primary_location") or {}
    source = primary.get("source") or {}
    return clean_text(source.get("display_name") or "")


def source_url(work):
    primary = work.get("primary_location") or {}
    return primary.get("landing_page_url") or work.get("id") or ""


def infer_notes(work):
    title = clean_text(work.get("title") or "")
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    blob = f"{title} {abstract}".lower()
    hits = []
    for label, keywords in [
        ("sen", SEN_KW),
        ("adaptive", ADAPT_KW),
        ("ai_analytics", AI_KW),
        ("observable_signal", SIGNAL_KW),
    ]:
        if has_any(blob, keywords):
            hits.append(label)
    return "openalex-round3-sen; hits=" + ",".join(hits)


def pick_candidates(group):
    results = []
    seen = set()
    for strict in (True, False):
        for query in group["queries"]:
            url = (
                f"{BASE_URL}?search={urllib.parse.quote(query)}"
                "&filter=from_publication_date:2020-01-01,has_abstract:true,is_paratext:false"
                "&sort=relevance_score:desc&per-page=100"
            )
            data = fetch_json(url)
            for work in data.get("results", []):
                work_id = work.get("id") or ""
                if not work_id or work_id in seen:
                    continue
                title = clean_text(work.get("title") or "")
                year = work.get("publication_year") or ""
                work_venue = venue(work)
                url_value = source_url(work)
                if not title or not year or not work_venue or not url_value:
                    continue
                if int(year) < 2020:
                    continue
                if not relevant(work, strict=strict):
                    continue
                seen.add(work_id)
                results.append((query, work))
                if len(results) >= group["target"]:
                    return results
    return results


def main():
    all_rows = []
    summary = []

    for group in GROUPS:
        picked = pick_candidates(group)
        summary.append((group["bucket"], len(picked)))
        for index, (query, work) in enumerate(picked, start=1):
            record_id = f"{group['prefix']}{index:03d}"
            domains = group["domains"]
            all_rows.append(
                {
                    "record_id": record_id,
                    "bucket": group["bucket"],
                    "query_string": query,
                    "title": clean_text(work.get("title") or ""),
                    "authors": author_str(work),
                    "year": work.get("publication_year") or "",
                    "venue": venue(work),
                    "publication_type": pub_type(work),
                    "doi": parse_doi(work),
                    "source_url": source_url(work),
                    "citation_count": work.get("cited_by_count") or 0,
                    "citation_date": TODAY,
                    "domain_sen": domains[0],
                    "domain_education": domains[1],
                    "domain_adaptive": domains[2],
                    "domain_ai_analytics": domains[3],
                    "domain_observable_signal": domains[4],
                    "study_type": "",
                    "sample_size": "",
                    "population_type": "",
                    "input_signal": "",
                    "ai_method": "",
                    "prediction_target": "",
                    "evaluation_metrics": "",
                    "decision": "",
                    "decision_reason": "",
                    "notes": infer_notes(work),
                }
            )

    with OUT_CSV.open("w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(all_rows)

    with OUT_LOG.open("w", encoding="utf-8") as file:
        file.write("# Round 3 SEN Collection Log\n\n")
        file.write(f"- Date: {TODAY}\n")
        file.write("- Source: OpenAlex API\n")
        file.write("- Filter: 2020+, has abstract, non-paratext\n")
        file.write("- Purpose: SEN/SEND-focused incremental search after supervisor terminology feedback\n")
        for bucket, count in summary:
            file.write(f"- {bucket}: {count}\n")
        file.write(f"- Total rows: {len(all_rows)}\n")
        file.write("\n## Query Buckets\n\n")
        for group in GROUPS:
            file.write(f"### {group['bucket']}\n\n")
            for query in group["queries"]:
                file.write(f"- `{query}`\n")
            file.write("\n")

    print(f"round3_sen_rows={len(all_rows)}")
    for bucket, count in summary:
        print(f"{bucket}: {count}")


if __name__ == "__main__":
    main()