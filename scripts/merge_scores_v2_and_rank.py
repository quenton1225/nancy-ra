import csv
from pathlib import Path
from collections import Counter

BASE = Path(r"c:\Users\Quenton\Documents\Github\nancy-ra\docs")
IN_MASTER = BASE / "37_validated_master_v1.csv"
SCORE_FILES = [
    BASE / "41_scores_batch_01.csv",
    BASE / "42_scores_batch_02.csv",
    BASE / "43_scores_batch_03.csv",
    BASE / "44_scores_batch_04.csv",
    BASE / "45_scores_batch_05.csv",
    BASE / "46_scores_batch_06.csv",
]
OUT_MASTER = BASE / "47_validated_master_v2_scored.csv"
OUT_SUMMARY = BASE / "48_scoring_v2_summary.md"
OUT_BY_DOMAIN = BASE / "49_ranked_by_domain_v2.csv"
OUT_OVERALL = BASE / "50_ranked_overall_v2.csv"
OUT_TOP30 = BASE / "51_top30_must_read_v2.md"
OUT_RISK = BASE / "52_high_risk_records_v2.md"

SUSPECT_VENUE_KW = [
    "world journal of advanced research and reviews",
    "international journal of scientific research in science and technology",
    "metaverse basic and applied research",
    "journal of education review provision",
    "patterniq",
    "intechopen",
    "preprints.org",
    "zenodo",
]


def group_of(record_id: str) -> str:
    if record_id.startswith("PNE") or record_id.startswith("R2NE"):
        return "neurodivergent+education"
    if record_id.startswith("PNA") or record_id.startswith("R2NA"):
        return "neurodivergent+adaptive"
    if record_id.startswith("PEA") or record_id.startswith("R2EA"):
        return "education+adaptive"
    return "unknown"


def load_scores(paths):
    scores = {}
    for p in paths:
        rows = list(csv.DictReader(open(p, encoding="utf-8")))
        for r in rows:
            rid = r["record_id"].strip()
            scores[rid] = {
                "quality_rigor": r["quality_rigor"].strip(),
                "quality_transfer": r["quality_transfer"].strip(),
                "quality_repro_ethics": r["quality_repro_ethics"].strip(),
                "decision": r["decision"].strip(),
                "decision_reason": r["decision_reason"].strip(),
            }
    return scores


def balanced_score(r):
    qr = int(r.get("quality_rigor") or 0)
    qt = int(r.get("quality_transfer") or 0)
    qe = int(r.get("quality_repro_ethics") or 0)
    if qr == 0 and qt == 0 and qe == 0:
        return 0.0
    return round((qr + qt + qe) / 3.0, 4)


def main():
    rows = list(csv.DictReader(open(IN_MASTER, encoding="utf-8")))
    scores = load_scores(SCORE_FILES)

    filled = 0
    still_missing = []
    dec_counter = Counter()

    for r in rows:
        rid = r.get("record_id", "")
        if rid in scores:
            s = scores[rid]
            r["quality_rigor"] = s["quality_rigor"]
            r["quality_transfer"] = s["quality_transfer"]
            r["quality_repro_ethics"] = s["quality_repro_ethics"]
            r["decision"] = s["decision"]
            r["decision_reason"] = s["decision_reason"]
            filled += 1
        if not (r.get("decision") or "").strip():
            still_missing.append(rid)
        else:
            dec_counter[r["decision"]] += 1

        r["scored_group"] = group_of(rid)
        r["balanced_score"] = balanced_score(r)

    fields = list(rows[0].keys())
    with open(OUT_MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)

    tier_order = {"keep_high": 0, "keep_medium": 1, "maybe": 2, "exclude": 3}
    overall = sorted(
        rows,
        key=lambda x: (
            tier_order.get((x.get("decision") or "exclude"), 9),
            -float(x.get("balanced_score") or 0),
            -int(x.get("citation_count") or 0),
        ),
    )

    with open(OUT_OVERALL, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(overall)

    by_domain = []
    groups = ["neurodivergent+education", "neurodivergent+adaptive", "education+adaptive"]
    for g in groups:
        items = [r for r in rows if r.get("scored_group") == g]
        items = sorted(
            items,
            key=lambda x: (
                tier_order.get((x.get("decision") or "exclude"), 9),
                -float(x.get("balanced_score") or 0),
                -int(x.get("citation_count") or 0),
            ),
        )
        for i, it in enumerate(items, start=1):
            row = dict(it)
            row["domain_rank"] = i
            by_domain.append(row)

    fields_domain = list(by_domain[0].keys()) if by_domain else fields
    with open(OUT_BY_DOMAIN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields_domain)
        w.writeheader()
        w.writerows(by_domain)

    top30 = overall[:30]
    with open(OUT_TOP30, "w", encoding="utf-8") as f:
        f.write("# Top 30 Must-Read (v2)\n\n")
        f.write("Based on scored decisions and balanced score.\n\n")
        f.write("| Rank | Record ID | Group | Decision | Score | Citations | Title |\n")
        f.write("|---|---|---|---|---:|---:|---|\n")
        for i, r in enumerate(top30, start=1):
            title = (r.get("title") or "").replace("|", "/")
            f.write(
                f"| {i} | {r.get('record_id')} | {r.get('scored_group')} | {r.get('decision')} | {r.get('balanced_score')} | {r.get('citation_count')} | {title} |\n"
            )

    # High-risk list
    risk_rows = []
    for r in rows:
        v = (r.get("venue") or "").lower()
        s = (r.get("source_url") or "").lower()
        risk_reasons = []
        if any(k in v for k in SUSPECT_VENUE_KW):
            risk_reasons.append("suspect_venue")
        if "preprint" in v or "arxiv" in v or "preprints.org" in s:
            risk_reasons.append("preprint_source")
        if int(r.get("citation_count") or 0) == 0:
            risk_reasons.append("zero_citation")
        if (r.get("decision") or "") == "exclude":
            risk_reasons.append("decision_exclude")
        if risk_reasons:
            risk_rows.append((r, risk_reasons))

    with open(OUT_RISK, "w", encoding="utf-8") as f:
        f.write("# High Risk Records (v2)\n\n")
        f.write("Records flagged by venue/source/citation/decision heuristics.\n\n")
        f.write("| Record ID | Decision | Citations | Venue | Risk Reasons |\n")
        f.write("|---|---|---:|---|---|\n")
        for r, reasons in sorted(risk_rows, key=lambda x: x[0].get("record_id", "")):
            venue = (r.get("venue") or "").replace("|", "/")
            f.write(
                f"| {r.get('record_id')} | {r.get('decision')} | {r.get('citation_count')} | {venue} | {', '.join(reasons)} |\n"
            )

    with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write("# Scoring v2 Summary\n\n")
        f.write(f"- Input master rows: {len(rows)}\n")
        f.write(f"- Newly filled from pending batches: {filled}\n")
        f.write(f"- Rows still missing decision: {len(still_missing)}\n")
        f.write("\n## Decision Distribution\n")
        for k in ["keep_high", "keep_medium", "maybe", "exclude"]:
            f.write(f"- {k}: {dec_counter.get(k, 0)}\n")

    print(f"v2 done rows={len(rows)} missing={len(still_missing)}")


if __name__ == "__main__":
    main()
