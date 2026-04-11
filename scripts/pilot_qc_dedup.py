import csv
import datetime as dt
from collections import defaultdict

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_raw.csv"
OUT_CLEAN = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_cleaned.csv"
OUT_REPORT = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\14_pilot_qc_report.md"


def norm_title(t: str) -> str:
    return " ".join((t or "").strip().lower().split())


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    kept = []
    removed = []

    seen_doi = {}
    seen_title_year = {}

    for r in rows:
        doi = (r.get("doi") or "").strip().lower()
        title = norm_title(r.get("title", ""))
        year = (r.get("year") or "").strip()

        dedup_reason = ""
        group_id = ""

        if doi:
            if doi in seen_doi:
                dedup_reason = "duplicate_doi"
                group_id = seen_doi[doi]
            else:
                seen_doi[doi] = r["record_id"]
                group_id = r["record_id"]
        else:
            key = (title, year)
            if key in seen_title_year:
                dedup_reason = "duplicate_title_year"
                group_id = seen_title_year[key]
            else:
                seen_title_year[key] = r["record_id"]
                group_id = r["record_id"]

        if dedup_reason:
            r["dedup_group"] = group_id
            removed.append((r, dedup_reason))
        else:
            r["dedup_group"] = group_id
            kept.append(r)

    # Keep schema as-is
    fieldnames = rows[0].keys() if rows else []
    with open(OUT_CLEAN, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(kept)

    by_reason = defaultdict(int)
    for _, reason in removed:
        by_reason[reason] += 1

    today = dt.date.today().isoformat()
    with open(OUT_REPORT, "w", encoding="utf-8") as f:
        f.write("# Pilot QC Report\n\n")
        f.write(f"- Date: {today}\n")
        f.write(f"- Input rows: {len(rows)}\n")
        f.write(f"- Kept rows: {len(kept)}\n")
        f.write(f"- Removed rows: {len(removed)}\n")
        if removed:
            f.write("\n## Removal Summary\n")
            for k, v in sorted(by_reason.items()):
                f.write(f"- {k}: {v}\n")
            f.write("\n## Removed Records\n")
            for rec, reason in removed:
                f.write(
                    f"- {rec.get('record_id')} | {reason} | {rec.get('title','')[:120]}\n"
                )
        else:
            f.write("\nNo duplicates detected by exact DOI/title-year rules.\n")

    print(f"QC complete. kept={len(kept)} removed={len(removed)}")


if __name__ == "__main__":
    main()
