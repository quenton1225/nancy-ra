import csv
import statistics
import sys
from collections import defaultdict
from pathlib import Path


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def read_rows(path):
    with Path(path).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def summarize_trial(trial_id, rows):
    gaze_rows = [row for row in rows if row.get("event_type") == "gaze"]
    timestamps = [to_float(row.get("timestamp_ms")) for row in gaze_rows]
    timestamps = [value for value in timestamps if value is not None]
    xs = [to_float(row.get("gaze_x")) for row in gaze_rows]
    ys = [to_float(row.get("gaze_y")) for row in gaze_rows]
    width = max([to_float(row.get("page_width")) or 0 for row in gaze_rows] or [0])
    height = max([to_float(row.get("page_height")) or 0 for row in gaze_rows] or [0])

    valid_points = [(x, y) for x, y in zip(xs, ys) if x is not None and y is not None]
    onscreen = [(x, y) for x, y in valid_points if 0 <= x <= width and 0 <= y <= height]
    offscreen = len(valid_points) - len(onscreen)

    probe_rows = [row for row in rows if row.get("event_type") == "probe_answer"]
    probe = probe_rows[-1] if probe_rows else {}

    reading_duration = max(timestamps) - min(timestamps) if len(timestamps) >= 2 else 0
    valid_ratio = len(valid_points) / len(gaze_rows) if gaze_rows else 0
    offscreen_ratio = offscreen / len(valid_points) if valid_points else 0

    x_values = [x for x, _ in onscreen]
    y_values = [y for _, y in onscreen]
    gaze_dispersion_x = statistics.pstdev(x_values) if len(x_values) > 1 else 0
    gaze_dispersion_y = statistics.pstdev(y_values) if len(y_values) > 1 else 0

    return {
        "trial_id": trial_id,
        "gaze_samples": len(gaze_rows),
        "reading_duration_ms": round(reading_duration, 2),
        "valid_gaze_ratio": round(valid_ratio, 4),
        "offscreen_ratio": round(offscreen_ratio, 4),
        "gaze_dispersion_x": round(gaze_dispersion_x, 4),
        "gaze_dispersion_y": round(gaze_dispersion_y, 4),
        "probe_tut": probe.get("probe_tut", ""),
        "difficulty": probe.get("difficulty", ""),
        "familiarity": probe.get("familiarity", ""),
    }


def main():
    if len(sys.argv) != 3:
        print("Usage: python extract_features.py raw_gaze.csv features.csv")
        raise SystemExit(2)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    rows = read_rows(input_path)
    grouped = defaultdict(list)
    for row in rows:
        trial_id = row.get("trial_id") or "unknown"
        if trial_id.startswith("trial_"):
            grouped[trial_id].append(row)

    summaries = [summarize_trial(trial_id, trial_rows) for trial_id, trial_rows in sorted(grouped.items())]
    fieldnames = [
        "trial_id",
        "gaze_samples",
        "reading_duration_ms",
        "valid_gaze_ratio",
        "offscreen_ratio",
        "gaze_dispersion_x",
        "gaze_dispersion_y",
        "probe_tut",
        "difficulty",
        "familiarity",
    ]
    with Path(output_path).open("w", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(summaries)

    print(f"features={len(summaries)} output={output_path}")


if __name__ == "__main__":
    main()
