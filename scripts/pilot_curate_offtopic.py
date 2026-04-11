import csv
import datetime as dt

IN_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_cleaned.csv"
OUT_CSV = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\12_pilot_candidates_curated.csv"
OUT_LOG = r"c:\Users\Quenton\Documents\Github\nancy-ra\docs\16_pilot_exclusion_log.md"

OFFTOPIC_KEYWORDS = [
    "psk16 lattice quantization",
    "hardware-ready mitigation",
    "ci/cd",
    "containerized microservices",
]

OFFTOPIC_VENUE_KEYWORDS = [
    "zenodo",
]


def is_offtopic(row):
    title = (row.get("title") or "").lower()
    venue = (row.get("venue") or "").lower()

    if any(k in title for k in OFFTOPIC_KEYWORDS):
        return True, "offtopic_title_keyword"
    if any(k in venue for k in OFFTOPIC_VENUE_KEYWORDS):
        return True, "offtopic_venue_keyword"

    return False, ""


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    kept = []
    excluded = []

    for r in rows:
        bad, reason = is_offtopic(r)
        if bad:
            excluded.append((r, reason))
        else:
            kept.append(r)

    fields = rows[0].keys() if rows else []
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(kept)

    with open(OUT_LOG, "w", encoding="utf-8") as f:
        f.write("# Pilot Exclusion Log\n\n")
        f.write(f"- Date: {dt.date.today().isoformat()}\n")
        f.write(f"- Input rows: {len(rows)}\n")
        f.write(f"- Kept rows: {len(kept)}\n")
        f.write(f"- Excluded rows: {len(excluded)}\n")
        if excluded:
            f.write("\n## Excluded Records\n")
            for rec, reason in excluded:
                f.write(f"- {rec.get('record_id')} | {reason} | {rec.get('title')}\n")

    print(f"Curated rows: {len(kept)} (excluded {len(excluded)})")


if __name__ == "__main__":
    main()
