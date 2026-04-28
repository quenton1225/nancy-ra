# Eye Tracking Five-Sample Comparison

**日期**: 2026-04-28  
**对应 pilot log**: `69_eye_tracking_mvp_pilot_log_20260428.md`  
**样本**: P001, P002, P003, P004, P005  
**目的**: 将 P005 严格正常条件样本纳入比较，更新普通笔记本 WebGazer MVP 的可行性和数据质量判断。

## 1. 样本条件

| sample | 受试者/条件 | raw file | feature file | scanpath index |
| --- | --- | --- | --- | --- |
| P001 | 受试者 1 早期基线；正常光照 | `eye_tracking_demo/data/raw/reading_gaze_P001_S1777382254070.csv` | `eye_tracking_demo/data/processed/features_P001_S1777382254070.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P001_S1777382254070/index.html` |
| P002 | 受试者 1；戴眼镜；持续上下左右转头；正常光照 | `eye_tracking_demo/data/raw/reading_gaze_P002_S1777384531374.csv` | `eye_tracking_demo/data/processed/features_P002_S1777384531374.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P002_S1777384531374/index.html` |
| P003 | 受试者 2；不戴眼镜；正常光照；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P003_S1777385935863.csv` | `eye_tracking_demo/data/processed/features_P003_S1777385935863.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P003_S1777385935863/index.html` |
| P004 | 受试者 2；不戴眼镜；关闭台灯，略暗光、略逆光；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P004_S1777386312284.csv` | `eye_tracking_demo/data/processed/features_P004_S1777386312284.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P004_S1777386312284/index.html` |
| P005 | 受试者 1；不戴眼镜；正常光照；最严格避免转头，尽量只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P005_S1777388229181.csv` | `eye_tracking_demo/data/processed/features_P005_S1777388229181.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P005_S1777388229181/index.html` |

## 2. Raw-level summary

| sample | participant_id | raw rows | gaze rows | duration_s | avg_hz | offscreen_all | calibration | reading_gaze | probe_gaze | quiz_gaze | quiz_correct |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P001 | P001 | 8525 | 8494 | 169.8 | 50.0 | 0.0274 | 9 | 4080 | 1473 | 2389 | 3/3 |
| P002 | P002 | 3450 | 3419 | 124.6 | 27.4 | 0.0140 | 9 | 1833 | 545 | 606 | 2/3 |
| P003 | P003 | 12946 | 12915 | 260.1 | 49.6 | 0.0132 | 9 | 5108 | 3219 | 3733 | 2/3 |
| P004 | P004 | 6256 | 6225 | 124.6 | 50.0 | 0.0050 | 9 | 3982 | 925 | 711 | 2/3 |
| P005 | P005 | 5645 | 5614 | 118.0 | 47.6 | 0.0082 | 9 | 3586 | 472 | 715 | 3/3 |

## 3. Trial-level aggregate summary

| sample | mean reading ms | total reading s | mean gaze samples/trial | mean offscreen | mean disp x | mean disp y | TUT positive | mean difficulty | mean familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P001 | 36788 | 110.4 | 1851.0 | 0.0102 | 251.2 | 73.8 | 1/3 | 4.7 | 3.0 |
| P002 | 29817 | 89.5 | 792.7 | 0.0067 | 281.9 | 80.7 | 1/3 | 5.3 | 2.7 |
| P003 | 56316 | 168.9 | 2775.7 | 0.0059 | 271.8 | 98.5 | 3/3 | 4.7 | 2.3 |
| P004 | 32410 | 97.2 | 1635.7 | 0.0053 | 306.2 | 93.8 | 3/3 | 3.7 | 4.0 |
| P005 | 28792 | 86.4 | 1352.7 | 0.0033 | 252.1 | 75.1 | 0/3 | 4.0 | 4.0 |

## 4. P005 trial-level details

| trial | gaze_samples | reading_s | offscreen | disp_x | disp_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 1414 | 30.2 | 0.0099 | 251.4 | 121.2 | 0 | 4 | 4 |
| trial_2 | 1305 | 27.9 | 0.0000 | 258.8 | 53.8 | 0 | 4 | 4 |
| trial_3 | 1339 | 28.2 | 0.0000 | 246.1 | 50.1 | 0 | 4 | 4 |

## 5. Updated interpretation

### 5.1 P005 is the cleanest strict-condition baseline for participant 1

P005 is the most controlled run from participant 1: no glasses, normal lighting, and strict instruction to avoid head movement. It produced complete data, 3/3 quiz accuracy, stable subjective ratings, and no TUT-positive trials.

Compared with P002, which used the same participant but added glasses and continuous head turns, P005 has a much healthier sampling rate: 47.6Hz versus 27.4Hz. This strengthens the interpretation that head movement and/or glasses reduced P002 sampling density.

Compared with P001, P005 has lower overall offscreen ratio and similar horizontal dispersion, but shorter reading time and fewer reading gaze rows. P005 therefore looks like a cleaner but faster strict baseline, not simply a larger-data sample.

### 5.2 Participant 1 condition contrast is now clearer

For participant 1:

| contrast | P001 | P002 | P005 |
| --- | ---: | ---: | ---: |
| avg_hz | 50.0 | 27.4 | 47.6 |
| offscreen_all | 0.0274 | 0.0140 | 0.0082 |
| total reading s | 110.4 | 89.5 | 86.4 |
| TUT positive | 1/3 | 1/3 | 0/3 |
| quiz correct | 3/3 | 2/3 | 3/3 |

This gives a useful within-person comparison: the strict normal run is not the longest, but it is behaviorally and quality-wise clean.

### 5.3 P003 remains the largest data-volume sample

P003 still has the most raw rows and gaze rows, mainly because the participant spent much longer reading. It remains valuable for showing sustained WebGazer capture, while P005 is better as a controlled baseline for participant 1.

### 5.4 Updated quality conclusion

All five samples completed the full browser task and generated raw CSV, feature tables, and scanpath visualizations. Four of five samples stayed close to 48-50Hz; only P002 dropped substantially. This supports a practical feasibility claim: the MVP is robust enough for small pilot collection under normal use, but condition metadata is necessary for interpreting differences.

## 6. Methodological implication for next version

P005 makes the next design need even clearer. We should not keep relying on filename notes or chat memory for condition metadata. The next data schema should directly record:

1. participant repeat/run order;
2. lighting condition;
3. wearing glasses;
4. head movement instruction and observed compliance;
5. response timing;
6. calibration quality;
7. mouse, scroll, and AOI context.

With these fields, comparisons like P001 vs P002 vs P005 can be analyzed as condition contrasts rather than post-hoc notes.

## 7. Meeting-ready conclusion

> We now have five complete WebGazer pilot samples. The strictest participant-1 run, P005, performed well: 47.6Hz average gaze sampling, low offscreen ratio, 3/3 quiz accuracy, and no TUT-positive trials. Compared with P002, this strongly suggests that glasses plus head movement reduced sampling density. The demo is ready as a feasibility proof; the next step is richer condition and behavior logging before any model training.
