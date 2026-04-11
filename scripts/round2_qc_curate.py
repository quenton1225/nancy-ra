import csv
import datetime as dt
from collections import defaultdict

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\32_round2_candidates_raw.csv"
OUT_CLEAN = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\34_round2_candidates_cleaned.csv"
OUT_CURATED = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\35_round2_candidates_curated.csv"
OUT_REPORT = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\36_round2_qc_report.md"

OFFTOPIC_KEYWORDS = [
    "psk16 lattice quantization",
    "hardware-ready mitigation",
    "ci/cd",
    "containerized microservices",
    "food is medicine",
    "presidential advisory",
]

OFFTOPIC_VENUE = ["zenodo"]


def norm_title(t: str):
    return " ".join((t or "").strip().lower().split())


def is_offtopic(row):
    t = (row.get("title") or "").lower()
    v = (row.get("venue") or "").lower()
    if any(k in t for k in OFFTOPIC_KEYWORDS):
        return True, "offtopic_title"
    if any(k in v for k in OFFTOPIC_VENUE):
        return True, "offtopic_venue"
    return False, ""


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    fields = rows[0].keys() if rows else []

    # pass1 dedup
    kept = []
    removed = []
    seen_doi = {}
    seen_title_year = {}

    for r in rows:
        doi = (r.get("doi") or "").strip().lower()
        key = (norm_title(r.get("title", "")), (r.get("year") or "").strip())

        reason = ""
        grp = ""
        if doi:
            if doi in seen_doi:
                reason = "duplicate_doi"
                grp = seen_doi[doi]
            else:
                seen_doi[doi] = r["record_id"]
                grp = r["record_id"]
        else:
            if key in seen_title_year:
                reason = "duplicate_title_year"
                grp = seen_title_year[key]
            else:
                seen_title_year[key] = r["record_id"]
                grp = r["record_id"]

        if reason:
            r["dedup_group"] = grp
            removed.append((r, reason))
        else:
            r["dedup_group"] = grp
            kept.append(r)

    with open(OUT_CLEAN, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)

    # pass2 off-topic curation
    curated = []
    excluded = []
    for r in kept:
        bad, reason = is_offtopic(r)
        if bad:
            excluded.append((r, reason))
        else:
            curated.append(r)

    with open(OUT_CURATED, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(curated)

    by_reason = defaultdict(int)
    for _, reason in removed:
        by_reason[reason] += 1

    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        f.write("# Round2 QC Report\n\n")
        f.write(f"- Date: {dt.date.today().isoformat()}\n")
        f.write(f"- Raw input: {len(rows)}\n")
        f.write(f"- After dedup: {len(kept)}\n")
        f.write(f"- Dedup removed: {len(removed)}\n")
        for k, v in sorted(by_reason.items()):
            f.write(f"- {k}: {v}\n")
        f.write(f"- Curated output: {len(curated)}\n")
        f.write(f"- Off-topic excluded: {len(excluded)}\n")
        if excluded:
            f.write("\n## Off-topic Excluded\n")
            for rec, reason in excluded[:30]:
                f.write(f"- {rec.get('record_id')} | {reason} | {rec.get('title')}\n")

    print(f"Round2 QC done. clean={len(kept)} curated={len(curated)}")


if __name__ == "__main__":
    main()
