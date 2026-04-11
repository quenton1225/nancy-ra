import csv
from collections import defaultdict

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_curated.csv"
OUT_PNE = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\20_batch_pne.csv"
OUT_PNA = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\21_batch_pna.csv"
OUT_PEA = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\22_batch_pea.csv"
OUT_MD = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\20_scoring_batches.md"


def pick_bucket(record_id: str) -> str:
    p = (record_id or "")[:3]
    if p == "PNE":
        return "PNE"
    if p == "PNA":
        return "PNA"
    if p == "PEA":
        return "PEA"
    return "OTHER"


def write_csv(path, rows, fields):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    fields = rows[0].keys() if rows else []
    buckets = defaultdict(list)

    for r in rows:
        buckets[pick_bucket(r.get("record_id", ""))].append(r)

    write_csv(OUT_PNE, buckets["PNE"], fields)
    write_csv(OUT_PNA, buckets["PNA"], fields)
    write_csv(OUT_PEA, buckets["PEA"], fields)

    with open(OUT_MD, "w", encoding="utf-8") as f:
        f.write("# Scoring Batch Plan\n\n")
        f.write("## Batch Files\n")
        f.write(f"- docs/20_batch_pne.csv ({len(buckets['PNE'])} records)\n")
        f.write(f"- docs/21_batch_pna.csv ({len(buckets['PNA'])} records)\n")
        f.write(f"- docs/22_batch_pea.csv ({len(buckets['PEA'])} records)\n")
        f.write("\n## Scoring Output Contract\n")
        f.write("Each record must return:\n")
        f.write("- record_id\n")
        f.write("- quality_rigor (1-5)\n")
        f.write("- quality_transfer (1-5)\n")
        f.write("- quality_repro_ethics (1-5)\n")
        f.write("- decision (keep_high/keep_medium/maybe/exclude)\n")
        f.write("- decision_reason (<= 25 words)\n")

    print(
        f"Prepared batches: PNE={len(buckets['PNE'])}, PNA={len(buckets['PNA'])}, PEA={len(buckets['PEA'])}"
    )


if __name__ == "__main__":
    main()
