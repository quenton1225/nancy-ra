import csv
from pathlib import Path
from collections import Counter

BASE = Path(r"c:\Users\Quenton\Documents\Github\nancy-ra\docs")
IN_MASTER = BASE / "12_pilot_candidates_curated.csv"
SCORE_FILES = [BASE / "23_scores_pne.csv", BASE / "24_scores_pna.csv", BASE / "25_scores_pea.csv"]
OUT_MASTER = BASE / "26_pilot_candidates_scored.csv"
OUT_SUMMARY = BASE / "27_scoring_summary.md"


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


def main():
    master_rows = list(csv.DictReader(open(IN_MASTER, encoding="utf-8")))
    scores = load_scores(SCORE_FILES)

    scored = 0
    missing = []
    decision_counter = Counter()

    for r in master_rows:
        rid = r.get("record_id", "").strip()
        if rid in scores:
            s = scores[rid]
            r["quality_rigor"] = s["quality_rigor"]
            r["quality_transfer"] = s["quality_transfer"]
            r["quality_repro_ethics"] = s["quality_repro_ethics"]
            r["decision"] = s["decision"]
            r["decision_reason"] = s["decision_reason"]
            scored += 1
            decision_counter[s["decision"]] += 1
        else:
            missing.append(rid)

    fields = master_rows[0].keys() if master_rows else []
    with open(OUT_MASTER, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(master_rows)

    with open(OUT_SUMMARY, "w", encoding="utf-8") as f:
        f.write("# Scoring Summary\n\n")
        f.write(f"- Input records: {len(master_rows)}\n")
        f.write(f"- Scored records: {scored}\n")
        f.write(f"- Missing scores: {len(missing)}\n")
        f.write("\n## Decision Distribution\n")
        for k in ["keep_high", "keep_medium", "maybe", "exclude"]:
            f.write(f"- {k}: {decision_counter.get(k, 0)}\n")
        if missing:
            f.write("\n## Missing Record IDs\n")
            for rid in missing:
                f.write(f"- {rid}\n")

    print(f"Merged scores into {OUT_MASTER}")


if __name__ == "__main__":
    main()
