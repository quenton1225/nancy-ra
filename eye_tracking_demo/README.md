# Webcam Eye Tracking MVP

This is a local, low-risk WebGazer MVP for reading-task gaze collection.

## Run

From the repository root:

```powershell
c:/Users/Quenton/Documents/Github/nancy-ra/.venv/Scripts/python.exe -m http.server 8765 -d eye_tracking_demo
```

Open:

```text
http://localhost:8765
```

Use Chrome or Edge. Camera access requires `localhost` or HTTPS.

The demo vendors WebGazer 3.5.3 and the MediaPipe FaceMesh runtime under `vendor/` and `mediapipe/face_mesh/`. Keep those folders with the HTML files when moving or publishing the demo; otherwise WebGazer will fail while loading FaceMesh assets.

## Privacy Boundary

- The demo uses the webcam only in the browser.
- It exports gaze coordinates, task events, probe answers, and quiz answers.
- It does not save video, screenshots, or face images.
- Data stays local unless the exported CSV is manually shared.

## Output

Store downloaded CSV files under:

```text
eye_tracking_demo/data/raw/
```

Store extracted feature tables under:

```text
eye_tracking_demo/data/processed/
```

The exported CSV contains mixed gaze and event rows:

- gaze rows: `event_type=gaze`
- calibration rows: `event_type=calibration_click`
- task rows: `probe_answer`, `quiz_answer`, `phase_start`, `export`

## Feature Extraction

```powershell
c:/Users/Quenton/Documents/Github/nancy-ra/.venv/Scripts/python.exe eye_tracking_demo/analysis/extract_features.py eye_tracking_demo/data/raw/exported.csv eye_tracking_demo/data/processed/features.csv
```

## Scanpath Visualization

Generate SVG scanpath images for each phase/trial:

```powershell
c:/Users/Quenton/Documents/Github/nancy-ra/.venv/Scripts/python.exe eye_tracking_demo/analysis/render_scanpaths.py eye_tracking_demo/data/raw/exported.csv
```

The default output folder is:

```text
eye_tracking_demo/data/visualizations/<exported-file-name>/
```

Open `index.html` in that folder to review all generated scanpath views.
