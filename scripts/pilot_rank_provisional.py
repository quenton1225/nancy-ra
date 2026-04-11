import csv
import math
from collections import defaultdict

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_curated.csv"
OUT_BY_DOMAIN = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\17_ranked_by_domain_provisional.csv"
OUT_OVERALL = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\18_ranked_overall_provisional.csv"
OUT_TOP20 = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\19_top20_must_read_provisional.md"

SUSPICIOUS_VENUE_KW = [
    "world journal of advanced research and reviews",
    "international journal of scientific research in science and technology",
    "metaverse basic and applied research",
    "journal of education review provision",
    "patterniq",
]


def group_of(record_id: str) -> str:
    p = (record_id or "")[:3]
    if p == "PNE":
        return "neurodivergent+education"
    if p == "PNA":
        return "neurodivergent+adaptive"
    if p == "PEA":
        return "education+adaptive"
    return "unknown"


def venue_bonus(venue: str) -> float:
    v = (venue or "").lower()
    bonus = 0.0
    if any(k in v for k in ["acm", "chi", "computers & education", "expert systems with applications", "cortex", "plos one", "frontiers", "bmc"]):
        bonus += 0.35
    if "preprints" in v or "zenodo" in v:
        bonus -= 0.25
    if any(k in v for k in SUSPICIOUS_VENUE_KW):
        bonus -= 0.35
    return bonus


def year_bonus(year: int) -> float:
    if year >= 2024:
        return 0.15
    if year >= 2022:
        return 0.08
    return 0.0


def score_row(r):
    citations = int(r.get("citation_count") or 0)
    y = int(r.get("year") or 0)
    c = math.log10(citations + 1) / 3.0
    s = c + venue_bonus(r.get("venue", "")) + year_bonus(y)
    return round(s, 4)


def decision_from_score(score: float) -> str:
    if score >= 0.95:
        return "keep_high"
    if score >= 0.65:
        return "keep_medium"
    if score >= 0.45:
        return "maybe"
    return "exclude"


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))

    enriched = []
    for r in rows:
        s = score_row(r)
        d = decision_from_score(s)
        rr = dict(r)
        rr["provisional_group"] = group_of(r.get("record_id", ""))
        rr["provisional_score"] = s
        rr["provisional_decision"] = d
        enriched.append(rr)

    # Ranked overall
    overall = sorted(enriched, key=lambda x: x["provisional_score"], reverse=True)
    out_fields = list(rows[0].keys()) + ["provisional_group", "provisional_score", "provisional_decision"]
    with open(OUT_OVERALL, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        w.writerows(overall)

    # Ranked by domain
    grouped = defaultdict(list)
    for r in enriched:
        grouped[r["provisional_group"]].append(r)

    by_domain_rows = []
    for g, items in grouped.items():
        items_sorted = sorted(items, key=lambda x: x["provisional_score"], reverse=True)
        for i, it in enumerate(items_sorted, start=1):
            row = dict(it)
            row["domain_rank"] = i
            by_domain_rows.append(row)

    out_fields_domain = out_fields + ["domain_rank"]
    with open(OUT_BY_DOMAIN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields_domain)
        w.writeheader()
        w.writerows(by_domain_rows)

    # Top 20 markdown
    top20 = overall[:20]
    with open(OUT_TOP20, "w", encoding="utf-8") as f:
        f.write("# Top 20 Must-Read (Provisional)\n\n")
        f.write("This list is metadata-based triage (not full-text scoring).\n\n")
        f.write("| Rank | Record ID | Year | Venue | Citations | Score | Decision | Title |\n")
        f.write("|---|---|---|---|---:|---:|---|---|\n")
        for i, r in enumerate(top20, start=1):
            title = (r.get("title") or "").replace("|", "/")
            f.write(
                f"| {i} | {r.get('record_id')} | {r.get('year')} | {r.get('venue')} | {r.get('citation_count')} | {r.get('provisional_score')} | {r.get('provisional_decision')} | {title} |\n"
            )

    print(f"Wrote {len(overall)} overall rows")


if __name__ == "__main__":
    main()
