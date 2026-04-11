import csv
import datetime as dt
import json
import re
import urllib.parse
import urllib.request

BASE_URL = "https://api.openalex.org/works"
TODAY = dt.date.today().isoformat()
OUT_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_raw.csv"
OUT_LOG = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\13_pilot_collection_log.md"

SCHEMA = [
    "record_id",
    "title",
    "authors",
    "year",
    "venue",
    "publication_type",
    "doi",
    "arxiv_id",
    "source_url",
    "citation_count",
    "citation_date",
    "domain_neurodivergent",
    "domain_education",
    "domain_adaptive",
    "study_type",
    "sample_size",
    "population_type",
    "input_signal",
    "ai_method",
    "prediction_target",
    "evaluation_metrics",
    "quality_rigor",
    "quality_transfer",
    "quality_repro_ethics",
    "decision",
    "decision_reason",
    "dedup_group",
    "reviewer",
    "review_date",
    "notes",
]

GROUPS = [
    {
        "prefix": "PNE",
        "target": 20,
        "domains": (1, 1, 0),
        "queries": [
            "neurodivergent learners education machine learning",
            "autism ADHD learning analytics education",
            "neurodiversity classroom adaptive learning",
        ],
        "label": "Neurodivergent+Education",
    },
    {
        "prefix": "PNA",
        "target": 20,
        "domains": (1, 0, 1),
        "queries": [
            "neurodivergent adaptive system personalization",
            "autism ADHD adaptive interface reinforcement learning",
            "neurodiversity human computer interaction personalization",
        ],
        "label": "Neurodivergent+Adaptive",
    },
    {
        "prefix": "PEA",
        "target": 20,
        "domains": (0, 1, 1),
        "queries": [
            "adaptive learning system personalized education",
            "learning preference modeling educational technology",
            "reinforcement learning educational personalization",
        ],
        "label": "Education+Adaptive",
    },
]

NEURO_KW = [
    "neurodiverg",
    "autism",
    "adhd",
    "dyslex",
    "learning disab",
    "special need",
]

EDU_KW = [
    "education",
    "learning",
    "classroom",
    "student",
    "pedagog",
    "teaching",
    "lms",
    "e-learning",
    "tutor",
]

ADAPT_KW = [
    "adaptive",
    "personaliz",
    "recommend",
    "reinforcement learning",
    "intelligent tutoring",
    "user model",
    "preference",
]


def fetch_json(url: str):
    req = urllib.request.Request(url, headers={"User-Agent": "nancy-ra-pilot/1.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return json.loads(resp.read().decode("utf-8"))


def pub_type(work):
    t = (work.get("type") or "").lower()
    if t == "article":
        return "journal"
    if t in {"proceedings-article", "peer-review"}:
        return "conference"
    if t in {"preprint"}:
        return "preprint"
    return "review_article" if "review" in (work.get("title") or "").lower() else "journal"


def parse_doi(work):
    doi = work.get("doi") or ""
    if doi.startswith("https://doi.org/"):
        return doi.replace("https://doi.org/", "")
    return doi


def parse_arxiv_id(source_url: str):
    if "arxiv.org/abs/" in source_url:
        return source_url.rsplit("/", 1)[-1]
    return ""


def clean_text(s: str):
    if not s:
        return ""
    return re.sub(r"\s+", " ", s).strip()


def inverted_index_to_text(inv_idx):
    if not inv_idx:
        return ""
    pos_to_word = {}
    for word, positions in inv_idx.items():
        for p in positions:
            pos_to_word[p] = word
    if not pos_to_word:
        return ""
    max_pos = max(pos_to_word.keys())
    words = [pos_to_word.get(i, "") for i in range(max_pos + 1)]
    return clean_text(" ".join(words))


def has_any(text: str, keywords):
    t = (text or "").lower()
    return any(k in t for k in keywords)


def relevant_for_group(work, group_label: str, strict: bool = True):
    title = clean_text(work.get("title") or "")
    abstract = inverted_index_to_text(work.get("abstract_inverted_index"))
    blob = f"{title} {abstract}".lower()

    has_neuro = has_any(blob, NEURO_KW)
    has_edu = has_any(blob, EDU_KW)
    has_adapt = has_any(blob, ADAPT_KW)

    if group_label == "Neurodivergent+Education":
        if strict:
            return has_neuro and has_edu
        return has_neuro and (has_edu or has_adapt)

    if group_label == "Neurodivergent+Adaptive":
        if strict:
            return has_neuro and has_adapt
        return has_neuro and (has_adapt or has_edu)

    if group_label == "Education+Adaptive":
        if strict:
            return has_edu and has_adapt
        return has_edu or has_adapt

    return False


def author_str(work):
    names = []
    for a in work.get("authorships", [])[:8]:
        name = ((a.get("author") or {}).get("display_name") or "").strip()
        if name:
            names.append(name)
    return "; ".join(names)


def venue(work):
    primary = work.get("primary_location") or {}
    src = primary.get("source") or {}
    return clean_text(src.get("display_name") or "")


def source_url(work):
    primary = work.get("primary_location") or {}
    landing = primary.get("landing_page_url") or ""
    if landing:
        return landing
    return work.get("id") or ""


def pick_candidates(group):
    results = []
    seen = set()

    for strict in (True, False):
        for q in group["queries"]:
            encoded = urllib.parse.quote(q)
            url = (
                f"{BASE_URL}?search={encoded}"
                "&filter=from_publication_date:2020-01-01,has_abstract:true,is_paratext:false"
                "&sort=relevance_score:desc&per-page=100"
            )
            data = fetch_json(url)
            for w in data.get("results", []):
                wid = w.get("id") or ""
                if not wid or wid in seen:
                    continue

                title = clean_text(w.get("title") or "")
                year = w.get("publication_year") or ""
                v = venue(w)
                src = source_url(w)

                if not title or not year or not v or not src:
                    continue
                if int(year) < 2020:
                    continue
                if not relevant_for_group(w, group["label"], strict=strict):
                    continue

                seen.add(wid)
                results.append(w)
                if len(results) >= group["target"]:
                    break
            if len(results) >= group["target"]:
                break
        if len(results) >= group["target"]:
            break

    return results


def main():
    all_rows = []
    summary = []

    for group in GROUPS:
        picked = pick_candidates(group)
        summary.append((group["label"], len(picked)))

        for i, w in enumerate(picked, start=1):
            rid = f"{group['prefix']}{i:03d}"
            src = source_url(w)
            row = {
                "record_id": rid,
                "title": clean_text(w.get("title") or ""),
                "authors": author_str(w),
                "year": w.get("publication_year") or "",
                "venue": venue(w),
                "publication_type": pub_type(w),
                "doi": parse_doi(w),
                "arxiv_id": parse_arxiv_id(src),
                "source_url": src,
                "citation_count": w.get("cited_by_count") or 0,
                "citation_date": TODAY,
                "domain_neurodivergent": group["domains"][0],
                "domain_education": group["domains"][1],
                "domain_adaptive": group["domains"][2],
                "study_type": "",
                "sample_size": "",
                "population_type": "",
                "input_signal": "",
                "ai_method": "",
                "prediction_target": "",
                "evaluation_metrics": "",
                "quality_rigor": "",
                "quality_transfer": "",
                "quality_repro_ethics": "",
                "decision": "",
                "decision_reason": "",
                "dedup_group": "",
                "reviewer": "",
                "review_date": "",
                "notes": "openalex-pilot-collection",
            }
            all_rows.append(row)

    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(all_rows)

    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write("# Pilot Collection Log\n\n")
        f.write(f"- Date: {TODAY}\n")
        f.write("- Source: OpenAlex API\n")
        f.write("- Scope: 3 query families, target 20 each\n")
        for label, cnt in summary:
            f.write(f"- {label}: {cnt} records\n")
        f.write(f"- Total rows: {len(all_rows)}\n")

    print(f"Wrote {len(all_rows)} rows to {OUT_CSV}")


if __name__ == "__main__":
    main()
