import csv
import html
import math
import statistics
import sys
import textwrap
from collections import Counter, defaultdict
from pathlib import Path


PASSAGES = {
    "p1": "Adaptive learning systems adjust content, pacing, or support based on learner signals. In inclusive education, the goal is not to label students, but to notice when a learner may need a clearer explanation, a slower pace, or a different presentation format.",
    "p2": "Webcam-based eye tracking estimates where a learner is looking by using a standard camera. The signal is noisier than a research-grade eye tracker, but it can be useful for low-risk measures such as reading time, off-screen gaze, and attention shifts.",
    "p3": "A careful educational system should fail softly. If a model is uncertain, it should offer optional support rather than make high-stakes decisions. This principle is especially important when working with students who may have special educational needs.",
}


def to_float(value):
    try:
        return float(value)
    except (TypeError, ValueError):
        return None


def safe_name(value):
    cleaned = []
    for char in value:
        cleaned.append(char if char.isalnum() or char in "-_" else "_")
    return "".join(cleaned).strip("_") or "unknown"


def read_rows(path):
    with Path(path).open(encoding="utf-8", newline="") as file:
        return list(csv.DictReader(file))


def mode_number(rows, field, default):
    values = [int(float(row[field])) for row in rows if to_float(row.get(field))]
    if not values:
        return default
    return Counter(values).most_common(1)[0][0]


def group_gaze_rows(rows):
    grouped = defaultdict(list)
    for row in rows:
        if row.get("event_type") != "gaze":
            continue
        x = to_float(row.get("gaze_x"))
        y = to_float(row.get("gaze_y"))
        if x is None or y is None:
            continue
        phase = row.get("phase") or "unknown"
        trial_id = row.get("trial_id") or phase
        if phase == "calibration":
            group_id = "calibration"
        elif phase in {"reading", "probe"}:
            group_id = f"{phase}_{trial_id}"
        elif phase == "quiz":
            group_id = "quiz"
        else:
            group_id = f"{phase}_{trial_id}"
        grouped[(phase, group_id)].append(row)
    return grouped


def sample_points(points, limit):
    if len(points) <= limit:
        return points
    step = (len(points) - 1) / (limit - 1)
    return [points[round(index * step)] for index in range(limit)]


def gradient_color(index, total):
    if total <= 1:
        ratio = 0
    else:
        ratio = index / (total - 1)
    start = (37, 99, 235)
    end = (220, 38, 38)
    rgb = tuple(round(start[channel] + (end[channel] - start[channel]) * ratio) for channel in range(3))
    return "#%02x%02x%02x" % rgb


def svg_text(x, y, text, size=16, fill="#1f2933", weight="400", anchor="start"):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-family="Arial, Helvetica, sans-serif" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}">{html.escape(str(text))}</text>'


def svg_rect(x, y, width, height, fill="#fff", stroke="#d9dee7", radius=8, opacity=1):
    return f'<rect x="{x:.1f}" y="{y:.1f}" width="{width:.1f}" height="{height:.1f}" rx="{radius}" fill="{fill}" stroke="{stroke}" opacity="{opacity}" />'


def wrap_svg_text(x, y, text, max_chars, line_height=30, size=20, fill="#1f2933"):
    parts = []
    for offset, line in enumerate(textwrap.wrap(text, width=max_chars)):
        parts.append(svg_text(x, y + offset * line_height, line, size=size, fill=fill))
    return parts


def draw_common_page(parts, width, height, title, status):
    parts.append(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">')
    parts.append(svg_rect(0, 0, width, height, fill="#f6f7f9", stroke="none", radius=0))
    shell_width = min(1100, max(width - 32, 320))
    shell_x = (width - shell_width) / 2
    parts.append(svg_text(shell_x, 52, "Reading Gaze Pilot", size=24, weight="700"))
    parts.append(svg_text(shell_x, 78, status, size=14, fill="#52606d"))
    parts.append(f'<line x1="{shell_x:.1f}" y1="100" x2="{shell_x + shell_width:.1f}" y2="100" stroke="#d9dee7" />')
    parts.append(svg_rect(shell_x + shell_width - 190, 42, 80, 34, fill="#23395d", stroke="#23395d", radius=6))
    parts.append(svg_text(shell_x + shell_width - 150, 63, "Start", size=14, fill="#fff", anchor="middle"))
    parts.append(svg_rect(shell_x + shell_width - 100, 42, 100, 34, fill="#7b8794", stroke="#7b8794", radius=6, opacity=0.45))
    parts.append(svg_text(shell_x + shell_width - 50, 63, "Export CSV", size=14, fill="#fff", anchor="middle"))
    parts.append(svg_text(shell_x, height - 18, title, size=13, fill="#52606d"))
    return shell_x, shell_width


def draw_stage_background(parts, phase, group_id, rows, width, height):
    shell_x, shell_width = draw_common_page(parts, width, height, f"{phase} / {group_id}", phase.title())
    panel_x = shell_x
    panel_y = 124
    panel_w = shell_width
    panel_h = max(260, height - panel_y - 58)
    parts.append(svg_rect(panel_x, panel_y, panel_w, panel_h, fill="#fff", stroke="#d9dee7", radius=8))

    if phase == "calibration":
        parts.append(svg_text(panel_x + 24, panel_y + 40, "Calibration", size=20, weight="700"))
        area_x = panel_x + 24
        area_y = panel_y + 66
        area_w = panel_w - 48
        area_h = panel_h - 90
        parts.append(svg_rect(area_x, area_y, area_w, area_h, fill="#fbfcfd", stroke="#9aa5b1", radius=8, opacity=0.9))
        for index, (left, top) in enumerate([(10, 10), (50, 10), (90, 10), (10, 50), (50, 50), (90, 50), (10, 90), (50, 90), (90, 90)], 1):
            cx = area_x + area_w * left / 100
            cy = area_y + area_h * top / 100
            parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="17" fill="#fff" stroke="#d64545" stroke-width="3" />')
            parts.append(svg_text(cx, cy + 5, index, size=12, fill="#d64545", weight="700", anchor="middle"))
    elif phase == "reading":
        trial_number = group_id.split("_")[-1]
        text_id = rows[0].get("text_id") if rows else ""
        passage = PASSAGES.get(text_id, f"Passage {trial_number}")
        parts.append(svg_text(panel_x + 24, panel_y + 36, f"Passage {trial_number} / 3", size=16, fill="#323f4b"))
        parts.append(svg_rect(panel_x + panel_w - 120, panel_y + 18, 96, 36, fill="#23395d", stroke="#23395d", radius=6))
        parts.append(svg_text(panel_x + panel_w - 72, panel_y + 41, "Continue", size=14, fill="#fff", anchor="middle"))
        text_x = panel_x + max(80, (panel_w - 760) / 2)
        text_y = panel_y + 110
        parts.extend(wrap_svg_text(text_x, text_y, passage, max_chars=78, line_height=38, size=20))
    elif phase == "probe":
        parts.append(svg_text(panel_x + 24, panel_y + 42, "Quick Check", size=20, weight="700"))
        parts.extend(wrap_svg_text(panel_x + 24, panel_y + 86, "Just before this screen, were you thinking about something unrelated to the reading?", 80, size=14, line_height=22, fill="#323f4b"))
        parts.append(svg_rect(panel_x + 24, panel_y + 134, 360, 34, fill="#fff", stroke="#cbd2d9", radius=6))
        parts.append(svg_text(panel_x + 36, panel_y + 156, "No / Yes", size=14, fill="#52606d"))
        parts.append(svg_text(panel_x + 24, panel_y + 210, "Difficulty", size=14, fill="#323f4b"))
        parts.append(f'<line x1="{panel_x + 24:.1f}" y1="{panel_y + 238:.1f}" x2="{panel_x + 384:.1f}" y2="{panel_y + 238:.1f}" stroke="#9aa5b1" stroke-width="5" stroke-linecap="round" />')
        parts.append(svg_text(panel_x + 24, panel_y + 286, "Familiarity", size=14, fill="#323f4b"))
        parts.append(f'<line x1="{panel_x + 24:.1f}" y1="{panel_y + 314:.1f}" x2="{panel_x + 384:.1f}" y2="{panel_y + 314:.1f}" stroke="#9aa5b1" stroke-width="5" stroke-linecap="round" />')
    elif phase == "quiz":
        parts.append(svg_text(panel_x + 24, panel_y + 42, "Comprehension", size=20, weight="700"))
        questions = ["What is the safer goal for the pilot?", "Why should the system fail softly?", "What data does this MVP export?"]
        y = panel_y + 90
        for question in questions:
            parts.append(svg_rect(panel_x + 24, y - 24, min(680, panel_w - 48), 68, fill="#fff", stroke="#d9dee7", radius=6))
            parts.append(svg_text(panel_x + 42, y, question, size=15, fill="#323f4b"))
            parts.append(svg_rect(panel_x + 42, y + 14, 360, 28, fill="#fff", stroke="#cbd2d9", radius=6))
            y += 86
    else:
        parts.append(svg_text(panel_x + 24, panel_y + 42, phase.title(), size=20, weight="700"))


def draw_scanpath(parts, rows, width, height):
    points = []
    for row in rows:
        x = to_float(row.get("gaze_x"))
        y = to_float(row.get("gaze_y"))
        timestamp = to_float(row.get("timestamp_ms")) or 0
        if x is not None and y is not None:
            points.append((x, y, timestamp))
    if not points:
        parts.append(svg_text(24, height - 48, "No valid gaze points", size=16, fill="#dc2626"))
        return

    path_points = sample_points(points, 450)
    path_data = " ".join(("M" if index == 0 else "L") + f" {x:.1f} {y:.1f}" for index, (x, y, _) in enumerate(path_points))
    parts.append(f'<path d="{path_data}" fill="none" stroke="#2563eb" stroke-width="2" stroke-opacity="0.35" />')

    marker_points = sample_points(points, min(24, len(points)))
    for index, (x, y, _) in enumerate(marker_points, 1):
        color = gradient_color(index - 1, len(marker_points))
        parts.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{color}" fill-opacity="0.82" stroke="#fff" stroke-width="2" />')
        parts.append(svg_text(x, y + 4, index, size=8, fill="#fff", weight="700", anchor="middle"))

    start_x, start_y, _ = points[0]
    end_x, end_y, _ = points[-1]
    parts.append(f'<circle cx="{start_x:.1f}" cy="{start_y:.1f}" r="13" fill="none" stroke="#16a34a" stroke-width="4" />')
    parts.append(svg_text(start_x + 16, start_y - 12, "START", size=11, fill="#166534", weight="700"))
    parts.append(f'<circle cx="{end_x:.1f}" cy="{end_y:.1f}" r="13" fill="none" stroke="#dc2626" stroke-width="4" />')
    parts.append(svg_text(end_x + 16, end_y - 12, "END", size=11, fill="#991b1b", weight="700"))

    xs = [x for x, _, _ in points]
    ys = [y for _, y, _ in points]
    timestamps = [timestamp for _, _, timestamp in points]
    offscreen = sum(1 for x, y, _ in points if not (0 <= x <= width and 0 <= y <= height))
    duration = max(timestamps) - min(timestamps) if len(timestamps) > 1 else 0
    summary = f"samples={len(points)} duration={duration/1000:.1f}s offscreen={offscreen/len(points):.1%} x_sd={statistics.pstdev(xs):.1f} y_sd={statistics.pstdev(ys):.1f}"
    parts.append(svg_rect(20, 116, min(760, width - 40), 34, fill="#ffffff", stroke="#cbd2d9", radius=6, opacity=0.88))
    parts.append(svg_text(34, 139, summary, size=14, fill="#1f2933"))


def write_svg(path, phase, group_id, rows):
    width = mode_number(rows, "page_width", 1600)
    height = mode_number(rows, "page_height", 900)
    width = max(900, min(width, 2400))
    height = max(650, min(height, 1600))
    parts = []
    draw_stage_background(parts, phase, group_id, rows, width, height)
    draw_scanpath(parts, rows, width, height)
    parts.append("</svg>")
    path.write_text("\n".join(parts), encoding="utf-8")


def write_index(output_dir, generated_files, source_path):
    lines = [
        "<!doctype html>",
        "<html lang=\"en\">",
        "<head><meta charset=\"utf-8\"><title>Scanpath Visualizations</title>",
        "<style>body{font-family:Arial,Helvetica,sans-serif;margin:24px;background:#f6f7f9;color:#1f2933}a{color:#1d4ed8}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(360px,1fr));gap:18px}.card{background:#fff;border:1px solid #d9dee7;border-radius:8px;padding:14px}.card img{width:100%;border:1px solid #e5e7eb}</style></head>",
        "<body>",
        f"<h1>Scanpath Visualizations</h1><p>Source: {html.escape(str(source_path))}</p>",
        "<div class=\"grid\">",
    ]
    for file_path in generated_files:
        name = file_path.name
        lines.append(f"<section class=\"card\"><h2>{html.escape(name)}</h2><a href=\"{html.escape(name)}\"><img src=\"{html.escape(name)}\" alt=\"{html.escape(name)}\"></a></section>")
    lines.extend(["</div>", "</body></html>"])
    (output_dir / "index.html").write_text("\n".join(lines), encoding="utf-8")


def chronological_key(item):
    (phase, group_id), group_rows = item
    first_timestamp = min((to_float(row.get("timestamp_ms")) or 0 for row in group_rows), default=0)
    phase_order = {"calibration": 0, "reading": 1, "probe": 2, "quiz": 3, "done": 4}
    return (first_timestamp, phase_order.get(phase, 99), group_id)


def main():
    if len(sys.argv) not in {2, 3}:
        print("Usage: python render_scanpaths.py raw_gaze.csv [output_dir]")
        raise SystemExit(2)

    input_path = Path(sys.argv[1])
    if len(sys.argv) == 3:
        output_dir = Path(sys.argv[2])
    else:
        output_dir = input_path.parents[1] / "visualizations" / input_path.stem
    output_dir.mkdir(parents=True, exist_ok=True)

    rows = read_rows(input_path)
    grouped = group_gaze_rows(rows)
    generated = []
    for (phase, group_id), group_rows in sorted(grouped.items(), key=chronological_key):
        filename = f"scanpath_{safe_name(group_id)}.svg"
        path = output_dir / filename
        write_svg(path, phase, group_id, group_rows)
        generated.append(path)

    write_index(output_dir, generated, input_path)
    print(f"visualizations={len(generated)} output_dir={output_dir}")


if __name__ == "__main__":
    main()
