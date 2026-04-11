import csv
import math
from pathlib import Path

BASE = Path(r"c:\Users\Quenton\Documents\Github\nancy-ra\docs")
IN_CSV = BASE / "37_validated_master_v1.csv"
OUT_PLAN = BASE / "39_pending_scoring_batches.md"


def main():
    rows = list(csv.DictReader(open(IN_CSV, encoding="utf-8")))
    pending = [r for r in rows if not (r.get("decision") or "").strip()]

    n_batches = 6
    batch_size = math.ceil(len(pending) / n_batches) if pending else 0

    files = []
    for i in range(n_batches):
        start = i * batch_size
        end = start + batch_size
        batch = pending[start:end]
        out = BASE / f"40_pending_batch_{i+1:02d}.csv"
        files.append((out, len(batch)))

        if batch:
            fields = batch[0].keys()
            with open(out, "w", newline="", encoding="utf-8") as f:
                w = csv.DictWriter(f, fieldnames=fields)
                w.writeheader()
                w.writerows(batch)
        else:
            with open(out, "w", newline="", encoding="utf-8") as f:
                f.write("record_id\n")

    with open(OUT_PLAN, "w", encoding="utf-8") as f:
        f.write("# Pending Scoring Batches (v2)\n\n")
        f.write(f"- Source: docs/37_validated_master_v1.csv\n")
        f.write(f"- Pending records: {len(pending)}\n")
        f.write(f"- Number of batches: {n_batches}\n")
        f.write(f"- Approx batch size: {batch_size}\n\n")
        f.write("## Batch Files\n")
        for path, size in files:
            f.write(f"- docs/{path.name} ({size} records)\n")

    print(f"pending={len(pending)} batches={n_batches} batch_size={batch_size}")


if __name__ == "__main__":
    main()
