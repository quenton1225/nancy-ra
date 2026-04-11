import csv
from pathlib import Path

BASE = Path(r"c:\Users\Quenton\Documents\Github\nancy-ra\docs")
PILOT = BASE / "26_pilot_candidates_scored.csv"
ROUND2 = BASE / "35_round2_candidates_curated.csv"
OUT = BASE / "37_validated_master_v1.csv"
REPORT = BASE / "38_validated_master_report.md"


def norm_title(t):
    return " ".join((t or "").strip().lower().split())


def load_rows(path):
    return list(csv.DictReader(open(path, encoding="utf-8")))


def main():
    pilot_rows = load_rows(PILOT)
    r2_rows = load_rows(ROUND2)

    all_rows = []
    seen_doi = set()
    seen_ty = set()

    # Prefer scored pilot rows when collisions happen
    source_order = [pilot_rows, r2_rows]

    for source_rows in source_order:
        for r in source_rows:
            doi = (r.get("doi") or "").strip().lower()
            ty = (norm_title(r.get("title", "")), (r.get("year") or "").strip())

            if doi and doi in seen_doi:
                continue
            if ty in seen_ty:
                continue

            if doi:
                seen_doi.add(doi)
            seen_ty.add(ty)
            all_rows.append(r)

    fields = all_rows[0].keys() if all_rows else []
    with open(OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(all_rows)

    # Stats
    scored = sum(1 for r in all_rows if (r.get("decision") or "").strip())
    with open(REPORT, "w", encoding="utf-8") as f:
        f.write("# Validated Master v1 Report\n\n")
        f.write(f"- Pilot input rows: {len(pilot_rows)}\n")
        f.write(f"- Round2 input rows: {len(r2_rows)}\n")
        f.write(f"- Output rows after cross-set dedup: {len(all_rows)}\n")
        f.write(f"- Rows with decision already filled: {scored}\n")
        f.write(f"- Rows pending scoring: {len(all_rows) - scored}\n")

    print(f"validated master rows: {len(all_rows)}")


if __name__ == "__main__":
    main()
