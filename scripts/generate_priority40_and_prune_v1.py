import csv
from pathlib import Path
from collections import defaultdict

BASE = Path(r"c:\Users\Quenton\Documents\Github\nancy-ra\docs")
IN_MASTER = BASE / "47_validated_master_v2_scored.csv"

OUT_PRIORITY_CSV = BASE / "53_fulltext_priority40_balanced.csv"
OUT_PRIORITY_MD = BASE / "53_fulltext_priority40_balanced.md"
OUT_PRUNE_MD = BASE / "54_prune_recommendations_v1.md"

SUSPECT_VENUE_KW = [
    "world journal of advanced research and reviews",
    "international journal of scientific research in science and technology",
    "metaverse basic and applied research",
    "journal of education review provision",
    "patterniq",
    "intechopen",
    "zenodo",
    "institutional repositories database",
    "revista tópicos",
    "annals of the romanian society for cell biology",
]


def group_of(record_id: str) -> str:
    if record_id.startswith("PNE") or record_id.startswith("R2NE"):
        return "neurodivergent+education"
    if record_id.startswith("PNA") or record_id.startswith("R2NA"):
        return "neurodivergent+adaptive"
    if record_id.startswith("PEA") or record_id.startswith("R2EA"):
        return "education+adaptive"
    return "unknown"


def decision_tier(decision: str) -> int:
    order = {"keep_high": 0, "keep_medium": 1, "maybe": 2, "exclude": 3}
    return order.get((decision or "exclude").strip(), 9)


def score(r):
    qr = int(r.get("quality_rigor") or 0)
    qt = int(r.get("quality_transfer") or 0)
    qe = int(r.get("quality_repro_ethics") or 0)
    return (qr + qt + qe) / 3.0 if (qr + qt + qe) else 0.0


def is_preprint(r):
    v = (r.get("venue") or "").lower()
    u = (r.get("source_url") or "").lower()
    p = (r.get("publication_type") or "").lower()
    return "arxiv" in v or "preprint" in v or "preprints.org" in u or p == "preprint"


def suspect_venue(r):
    v = (r.get("venue") or "").lower()
    return any(k in v for k in SUSPECT_VENUE_KW)


def pick_priority40(rows):
    # Use only keep_high + keep_medium
    candidates = [
        r for r in rows if (r.get("decision") in {"keep_high", "keep_medium"})
    ]

    for r in candidates:
        r["scored_group"] = group_of(r.get("record_id", ""))
        r["balanced_score"] = round(score(r), 4)

    grouped = defaultdict(list)
    for r in candidates:
        grouped[r["scored_group"]].append(r)

    for g in grouped:
        grouped[g] = sorted(
            grouped[g],
            key=lambda x: (
                decision_tier(x.get("decision", "")),
                -float(x.get("balanced_score", 0)),
                -int(x.get("citation_count") or 0),
            ),
        )

    # Balanced quota: 14 + 13 + 13 = 40
    quotas = {
        "education+adaptive": 14,
        "neurodivergent+adaptive": 13,
        "neurodivergent+education": 13,
    }

    selected = []
    selected_ids = set()

    for g, q in quotas.items():
        for r in grouped.get(g, [])[:q]:
            selected.append(r)
            selected_ids.add(r["record_id"])

    # Backfill if any group has fewer than quota
    if len(selected) < 40:
        rest = [
            r
            for r in sorted(
                candidates,
                key=lambda x: (
                    decision_tier(x.get("decision", "")),
                    -float(x.get("balanced_score", 0)),
                    -int(x.get("citation_count") or 0),
                ),
            )
            if r["record_id"] not in selected_ids
        ]
        need = 40 - len(selected)
        selected.extend(rest[:need])

    selected = sorted(
        selected,
        key=lambda x: (
            decision_tier(x.get("decision", "")),
            -float(x.get("balanced_score", 0)),
            -int(x.get("citation_count") or 0),
        ),
    )
    return selected[:40]


def build_prune_lists(rows):
    remove_now = []
    review_then_remove = []
    caution_hold = []

    for r in rows:
        dec = (r.get("decision") or "").strip()
        citations = int(r.get("citation_count") or 0)
        s_venue = suspect_venue(r)
        p_src = is_preprint(r)

        reasons = []
        if dec == "exclude":
            reasons.append("decision_exclude")
        if s_venue:
            reasons.append("suspect_venue")
        if p_src:
            reasons.append("preprint_source")
        if citations == 0:
            reasons.append("zero_citation")

        if dec == "exclude":
            if citations <= 20 or s_venue or p_src:
                remove_now.append((r, reasons))
            else:
                review_then_remove.append((r, reasons))
        elif dec == "maybe" and (s_venue or p_src or citations == 0):
            caution_hold.append((r, reasons))

    return remove_now, review_then_remove, caution_hold


def main():
    rows = list(csv.DictReader(open(IN_MASTER, encoding="utf-8")))

    for r in rows:
        r["scored_group"] = group_of(r.get("record_id", ""))
        r["balanced_score"] = round(score(r), 4)

    # Priority 40
    p40 = pick_priority40(rows)
    out_fields = [
        "record_id",
        "scored_group",
        "decision",
        "balanced_score",
        "citation_count",
        "year",
        "venue",
        "title",
        "source_url",
    ]

    with open(OUT_PRIORITY_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=out_fields)
        w.writeheader()
        for r in p40:
            w.writerow({k: r.get(k, "") for k in out_fields})

    with open(OUT_PRIORITY_MD, "w", encoding="utf-8") as f:
        f.write("# Full-Text Priority 40 (Balanced)\n\n")
        f.write("Balanced quotas across 3 domain-pairs, selected from keep_high and keep_medium.\n\n")
        f.write("| Rank | Record ID | Group | Decision | Score | Citations | Year | Title |\n")
        f.write("|---|---|---|---|---:|---:|---:|---|\n")
        for i, r in enumerate(p40, start=1):
            title = (r.get("title") or "").replace("|", "/")
            f.write(
                f"| {i} | {r.get('record_id')} | {r.get('scored_group')} | {r.get('decision')} | {r.get('balanced_score')} | {r.get('citation_count')} | {r.get('year')} | {title} |\n"
            )

    # Prune suggestions
    remove_now, review_then_remove, caution_hold = build_prune_lists(rows)

    with open(OUT_PRUNE_MD, "w", encoding="utf-8") as f:
        f.write("# Prune Recommendations v1\n\n")
        f.write("Heuristic categories: remove now, review then remove, caution hold.\n\n")

        f.write(f"## Remove Now ({len(remove_now)})\n\n")
        f.write("| Record ID | Decision | Citations | Venue | Reasons |\n")
        f.write("|---|---|---:|---|---|\n")
        for r, reasons in sorted(remove_now, key=lambda x: x[0].get("record_id", "")):
            venue = (r.get("venue") or "").replace("|", "/")
            f.write(f"| {r.get('record_id')} | {r.get('decision')} | {r.get('citation_count')} | {venue} | {', '.join(reasons)} |\n")

        f.write(f"\n## Review Then Remove ({len(review_then_remove)})\n\n")
        f.write("| Record ID | Decision | Citations | Venue | Reasons |\n")
        f.write("|---|---|---:|---|---|\n")
        for r, reasons in sorted(review_then_remove, key=lambda x: x[0].get("record_id", "")):
            venue = (r.get("venue") or "").replace("|", "/")
            f.write(f"| {r.get('record_id')} | {r.get('decision')} | {r.get('citation_count')} | {venue} | {', '.join(reasons)} |\n")

        f.write(f"\n## Caution Hold ({len(caution_hold)})\n\n")
        f.write("| Record ID | Decision | Citations | Venue | Reasons |\n")
        f.write("|---|---|---:|---|---|\n")
        for r, reasons in sorted(caution_hold, key=lambda x: x[0].get("record_id", "")):
            venue = (r.get("venue") or "").replace("|", "/")
            f.write(f"| {r.get('record_id')} | {r.get('decision')} | {r.get('citation_count')} | {venue} | {', '.join(reasons)} |\n")

    print(f"priority40={len(p40)} remove_now={len(remove_now)} review_then_remove={len(review_then_remove)} caution_hold={len(caution_hold)}")


if __name__ == "__main__":
    main()
