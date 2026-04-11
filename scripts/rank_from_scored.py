import csv
from collections import defaultdict

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\26_pilot_candidates_scored.csv"
OUT_BY_DOMAIN = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\28_ranked_by_domain_scored.csv"
OUT_OVERALL = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\29_ranked_overall_scored.csv"
OUT_TOP20 = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\30_top20_must_read_scored.md"


def group_of(record_id: str) -> str:
    p = (record_id or "")[:3]
    if p == "PNE":
        return "neurodivergent+education"
    if p == "PNA":
        return "neurodivergent+adaptive"
    if p == "PEA":
        return "education+adaptive"
    return "unknown"


def score(r):
    # Balanced weighting
    qr = int(r.get("quality_rigor") or 0)
    qt = int(r.get("quality_transfer") or 0)
    qe = int(r.get("quality_repro_ethics") or 0)
    return round((qr + qt + qe) / 3.0, 4)


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))

    for r in rows:
        r["scored_group"] = group_of(r.get("record_id", ""))
        r["balanced_score"] = score(r)

    # Overall ranking: decision tier first, then balanced score, then citation
    tier_order = {"keep_high": 0, "keep_medium": 1, "maybe": 2, "exclude": 3}
    overall = sorted(
        rows,
        key=lambda x: (
            tier_order.get(x.get("decision", "exclude"), 9),
            -x["balanced_score"],
            -int(x.get("citation_count") or 0),
        ),
    )

    fields = list(rows[0].keys())
    with open(OUT_OVERALL, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(overall)

    grouped = defaultdict(list)
    for r in rows:
        grouped[r["scored_group"]].append(r)

    by_domain = []
    for g, items in grouped.items():
        items_sorted = sorted(
            items,
            key=lambda x: (
                tier_order.get(x.get("decision", "exclude"), 9),
                -x["balanced_score"],
                -int(x.get("citation_count") or 0),
            ),
        )
        for i, r in enumerate(items_sorted, start=1):
            rr = dict(r)
            rr["domain_rank"] = i
            by_domain.append(rr)

    fields_domain = list(by_domain[0].keys()) if by_domain else []
    with open(OUT_BY_DOMAIN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields_domain)
        w.writeheader()
        w.writerows(by_domain)

    top20 = overall[:20]
    with open(OUT_TOP20, "w", encoding="utf-8") as f:
        f.write("# Top 20 Must-Read (Scored)\n\n")
        f.write("Based on balanced score from rigor/transfer/repro-ethics and decision tier.\n\n")
        f.write("| Rank | Record ID | Group | Decision | Score | Citations | Title |\n")
        f.write("|---|---|---|---|---:|---:|---|\n")
        for i, r in enumerate(top20, start=1):
            title = (r.get("title") or "").replace("|", "/")
            f.write(
                f"| {i} | {r.get('record_id')} | {r.get('scored_group')} | {r.get('decision')} | {r.get('balanced_score')} | {r.get('citation_count')} | {title} |\n"
            )

    print(f"Ranked {len(rows)} records")


if __name__ == "__main__":
    main()
