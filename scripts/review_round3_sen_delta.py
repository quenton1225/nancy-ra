import csv
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

RAW = DOCS / "64_round3_sen_candidates_raw.csv"
MASTER = DOCS / "47_validated_master_v2_scored.csv"
OUT_CSV = DOCS / "65_sen_delta_review_20260428.csv"
OUT_MD = DOCS / "65_sen_delta_review_20260428.md"

SCHEMA = [
    "record_id",
    "bucket",
    "delta_status",
    "priority_score",
    "citation_count",
    "year",
    "venue",
    "title",
    "doi",
    "source_url",
    "query_string",
    "auto_reason",
    "suggested_decision",
]

SEN_TERMS = [
    "special educational need",
    "special education need",
    "sen",
    "send",
    "learning disab",
    "learning difficult",
    "functional diversity",
    "inclusive education",
    "universal design for learning",
    "udl",
    "neurodivers",
    "neurodiverg",
]

TECH_TERMS = [
    "artificial intelligence",
    "machine learning",
    "learning analytics",
    "educational data mining",
    "adaptive",
    "personalized",
    "personalised",
    "assistive technolog",
    "education technology",
    "educational technology",
    "intelligent tutoring",
]

SIGNAL_TERMS = [
    "eye tracking",
    "gaze",
    "cognitive load",
    "prediction",
    "predicting",
    "classification",
    "behavioral",
    "behavioural",
    "interaction log",
]

WEAK_TERMS = [
    "covid",
    "pandemic",
    "zoom fatigue",
    "editorial",
    "advocating for children",
    "metaverse taxonomy",
    "federated learning",
    "causal inference",
    "materials science",
    "chemistry",
    "model predictive control for buildings",
    "entrepreneurship education",
    "categorical data for neural networks",
    "deep learning modelling techniques",
]

STRONG_VENUES = [
    "british journal of educational technology",
    "computers & education",
    "computers and education",
    "education and information technologies",
    "international journal of educational technology in higher education",
    "learning disabilities research and practice",
    "acm",
    "learning analytics",
    "educational data mining",
    "ieee",
]


def read_csv(path):
    with path.open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def normalize_title(value):
    text = (value or "").lower()
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"[^a-z0-9]+", " ", text)
    return re.sub(r"\s+", " ", text).strip()


def normalize_doi(value):
    text = (value or "").lower().strip()
    text = text.replace("https://doi.org/", "")
    return text.rstrip("/")


def has_any(text, terms):
    lowered = (text or "").lower()
    return any(term in lowered for term in terms)


def priority(row):
    title_blob = (row.get("title") or "").lower()
    venue_blob = (row.get("venue") or "").lower()
    blob = f"{title_blob} {venue_blob}"
    score = 0
    reasons = []

    if has_any(title_blob, SEN_TERMS):
        score += 2
        reasons.append("SEN/inclusion term")
    if has_any(title_blob, TECH_TERMS):
        score += 2
        reasons.append("AI/adaptive/edtech term")
    if has_any(title_blob, SIGNAL_TERMS):
        score += 2
        reasons.append("observable signal/prediction term")
    if has_any(venue_blob, STRONG_VENUES):
        score += 1
        reasons.append("strong/relevant venue")

    citations = int(row.get("citation_count") or 0)
    if citations >= 100:
        score += 1
        reasons.append("high citation")
    elif citations >= 25:
        score += 0.5
        reasons.append("moderate citation")

    if has_any(blob, WEAK_TERMS):
        score -= 2
        reasons.append("weak-topic penalty")

    return score, "; ".join(reasons)


def suggested_decision(delta_status, score):
    if delta_status != "new":
        return "duplicate_check"
    if score >= 5:
        return "screen_first"
    if score >= 3:
        return "screen_second"
    return "low_priority_or_noise"


def main():
    raw_rows = read_csv(RAW)
    master_rows = read_csv(MASTER)

    master_dois = {normalize_doi(row.get("doi")) for row in master_rows if normalize_doi(row.get("doi"))}
    master_titles = {normalize_title(row.get("title")) for row in master_rows if normalize_title(row.get("title"))}

    reviewed = []
    for row in raw_rows:
        doi = normalize_doi(row.get("doi"))
        title = normalize_title(row.get("title"))
        if doi and doi in master_dois:
            delta_status = "duplicate_doi"
        elif title and title in master_titles:
            delta_status = "duplicate_title"
        else:
            delta_status = "new"

        score, reason = priority(row)
        reviewed.append(
            {
                "record_id": row.get("record_id", ""),
                "bucket": row.get("bucket", ""),
                "delta_status": delta_status,
                "priority_score": score,
                "citation_count": row.get("citation_count", ""),
                "year": row.get("year", ""),
                "venue": row.get("venue", ""),
                "title": row.get("title", ""),
                "doi": row.get("doi", ""),
                "source_url": row.get("source_url", ""),
                "query_string": row.get("query_string", ""),
                "auto_reason": reason,
                "suggested_decision": suggested_decision(delta_status, score),
            }
        )

    reviewed.sort(
        key=lambda row: (
            row["delta_status"] != "new",
            -float(row["priority_score"]),
            -int(row["citation_count"] or 0),
            row["record_id"],
        )
    )

    with OUT_CSV.open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=SCHEMA)
        writer.writeheader()
        writer.writerows(reviewed)

    status_counts = Counter(row["delta_status"] for row in reviewed)
    bucket_counts = Counter(row["bucket"] for row in reviewed)
    bucket_new_counts = Counter(row["bucket"] for row in reviewed if row["delta_status"] == "new")
    decision_counts = Counter(row["suggested_decision"] for row in reviewed)
    top_new = [row for row in reviewed if row["delta_status"] == "new"][:20]

    by_bucket = defaultdict(list)
    for row in reviewed:
        if row["delta_status"] == "new" and len(by_bucket[row["bucket"]]) < 8:
            by_bucket[row["bucket"]].append(row)

    with OUT_MD.open("w", encoding="utf-8") as file:
        file.write("# SEN Round 3 Delta Review\n\n")
        file.write("## Summary\n\n")
        file.write(f"- Raw candidates: {len(reviewed)}\n")
        file.write(f"- New by DOI/title: {status_counts.get('new', 0)}\n")
        file.write(f"- Duplicate DOI: {status_counts.get('duplicate_doi', 0)}\n")
        file.write(f"- Duplicate title: {status_counts.get('duplicate_title', 0)}\n")
        file.write("\n## Bucket Counts\n\n")
        file.write("| Bucket | Raw | New |\n")
        file.write("| --- | ---: | ---: |\n")
        for bucket in sorted(bucket_counts):
            file.write(f"| {bucket} | {bucket_counts[bucket]} | {bucket_new_counts[bucket]} |\n")
        file.write("\n## Suggested Decisions\n\n")
        file.write("| Suggested decision | Count |\n")
        file.write("| --- | ---: |\n")
        for decision, count in sorted(decision_counts.items()):
            file.write(f"| {decision} | {count} |\n")

        file.write("\n## Top New Candidates for First Screening\n\n")
        file.write("| Record ID | Bucket | Score | Citations | Year | Title | Venue | Reason |\n")
        file.write("| --- | --- | ---: | ---: | ---: | --- | --- | --- |\n")
        for row in top_new:
            title = row["title"].replace("|", "/")
            venue = row["venue"].replace("|", "/")
            reason = row["auto_reason"].replace("|", "/")
            file.write(
                f"| {row['record_id']} | {row['bucket']} | {row['priority_score']} | "
                f"{row['citation_count']} | {row['year']} | {title} | {venue} | {reason} |\n"
            )

        file.write("\n## Top New Candidates by Bucket\n\n")
        for bucket in sorted(by_bucket):
            file.write(f"### {bucket}\n\n")
            file.write("| Record ID | Score | Citations | Year | Title | Venue |\n")
            file.write("| --- | ---: | ---: | ---: | --- | --- |\n")
            for row in by_bucket[bucket]:
                title = row["title"].replace("|", "/")
                venue = row["venue"].replace("|", "/")
                file.write(
                    f"| {row['record_id']} | {row['priority_score']} | {row['citation_count']} | "
                    f"{row['year']} | {title} | {venue} |\n"
                )
            file.write("\n")

        file.write("## Interpretation Notes\n\n")
        file.write("- This is an automatic delta and priority pass, not a final inclusion decision.\n")
        file.write("- High-priority rows should be checked manually for abstract fit, study design, and transfer value to Experiment 1A.\n")
        file.write("- COVID-only, policy-only, or general online learning rows should be downgraded unless they add a SEN-specific design variable.\n")

    print(f"reviewed={len(reviewed)} new={status_counts.get('new', 0)} duplicates={len(reviewed) - status_counts.get('new', 0)}")
    print(f"screen_first={decision_counts.get('screen_first', 0)} screen_second={decision_counts.get('screen_second', 0)}")


if __name__ == "__main__":
    main()