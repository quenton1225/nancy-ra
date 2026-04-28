# Eye Tracking Four-Sample Comparison

**日期**: 2026-04-28  
**对应 pilot log**: `69_eye_tracking_mvp_pilot_log_20260428.md`  
**样本**: P001, P002, P003, P004  
**状态**: 已由 `73_eye_tracking_five_sample_comparison_20260428.md` 继承；P005 加入后请优先阅读五样本报告。
**目的**: 比较正常光照、戴眼镜/转头、受试者 2 正常光照、受试者 2 略暗逆光四种条件下 WebGazer MVP 的数据质量。

## 1. 样本条件

| sample | 受试者/条件 | raw file | feature file | scanpath index |
| --- | --- | --- | --- | --- |
| P001 | 早期基线样本；光条件与 P002/P003 相同 | `eye_tracking_demo/data/raw/reading_gaze_P001_S1777382254070.csv` | `eye_tracking_demo/data/processed/features_P001_S1777382254070.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P001_S1777382254070/index.html` |
| P002 | 戴眼镜，持续上下左右转头；光条件与 P001/P003 相同 | `eye_tracking_demo/data/raw/reading_gaze_P002_S1777384531374.csv` | `eye_tracking_demo/data/processed/features_P002_S1777384531374.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P002_S1777384531374/index.html` |
| P003 | 受试者 2；不戴眼镜；正常光照；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P003_S1777385935863.csv` | `eye_tracking_demo/data/processed/features_P003_S1777385935863.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P003_S1777385935863/index.html` |
| P004 | 受试者 2；不戴眼镜；关闭台灯，略暗光、略逆光；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P004_S1777386312284.csv` | `eye_tracking_demo/data/processed/features_P004_S1777386312284.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P004_S1777386312284/index.html` |

## 2. Raw-level summary

| sample | participant_id | raw rows | gaze rows | duration_s | avg_hz | offscreen_all | calibration | reading_gaze | probe_gaze | quiz_gaze | quiz_correct |
| --- | --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P001 | P001 | 8525 | 8494 | 169.8 | 50.0 | 0.0274 | 9 | 4080 | 1473 | 2389 | 3/3 |
| P002 | P002 | 3450 | 3419 | 124.6 | 27.4 | 0.0140 | 9 | 1833 | 545 | 606 | 2/3 |
| P003 | P003 | 12946 | 12915 | 260.1 | 49.6 | 0.0132 | 9 | 5108 | 3219 | 3733 | 2/3 |
| P004 | P004 | 6256 | 6225 | 124.6 | 50.0 | 0.0050 | 9 | 3982 | 925 | 711 | 2/3 |

## 3. Trial-level aggregate summary

| sample | mean reading ms | total reading s | mean gaze samples/trial | mean offscreen | mean disp x | mean disp y | TUT positive | mean difficulty | mean familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P001 | 36788 | 110.4 | 1851.0 | 0.0102 | 251.2 | 73.8 | 1/3 | 4.7 | 3.0 |
| P002 | 29817 | 89.5 | 792.7 | 0.0067 | 281.9 | 80.7 | 1/3 | 5.3 | 2.7 |
| P003 | 56316 | 168.9 | 2775.7 | 0.0059 | 271.8 | 98.5 | 3/3 | 4.7 | 2.3 |
| P004 | 32410 | 97.2 | 1635.7 | 0.0053 | 306.2 | 93.8 | 3/3 | 3.7 | 4.0 |

## 4. Trial-level details

### P001

| trial | gaze_samples | reading_s | offscreen | disp_x | disp_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 2068 | 41.4 | 0.0058 | 235.0 | 94.6 | 0 | 6 | 2 |
| trial_2 | 1735 | 34.4 | 0.0110 | 249.4 | 58.1 | 0 | 4 | 3 |
| trial_3 | 1750 | 34.5 | 0.0137 | 269.2 | 68.7 | 1 | 4 | 4 |

### P002

| trial | gaze_samples | reading_s | offscreen | disp_x | disp_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 843 | 32.4 | 0.0178 | 302.7 | 100.3 | 0 | 5 | 3 |
| trial_2 | 701 | 26.6 | 0.0000 | 274.0 | 75.6 | 0 | 4 | 4 |
| trial_3 | 834 | 30.5 | 0.0024 | 269.0 | 66.2 | 1 | 7 | 1 |

### P003

| trial | gaze_samples | reading_s | offscreen | disp_x | disp_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 4192 | 86.0 | 0.0091 | 271.6 | 104.6 | 1 | 4 | 3 |
| trial_2 | 2481 | 50.2 | 0.0020 | 262.5 | 87.6 | 1 | 6 | 2 |
| trial_3 | 1654 | 32.8 | 0.0067 | 281.2 | 103.2 | 1 | 4 | 2 |

### P004

| trial | gaze_samples | reading_s | offscreen | disp_x | disp_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 1956 | 38.8 | 0.0000 | 279.5 | 102.1 | 1 | 5 | 4 |
| trial_2 | 1710 | 34.2 | 0.0158 | 349.5 | 84.2 | 1 | 3 | 4 |
| trial_3 | 1241 | 24.3 | 0.0000 | 289.5 | 95.2 | 1 | 3 | 4 |

## 5. Interpretation

### 5.1 P003: best data volume, but longer reading time

P003 has the highest raw row count, the highest gaze row count, and an average sampling rate close to 50Hz. It is currently the strongest sample for showing that the MVP can capture sustained gaze data when the participant avoids head movement and does not wear glasses.

However, P003 also has much longer reading time than the other samples. That makes the large gaze count partly a task-duration effect, not only a tracking-quality effect.

### 5.2 P004: dim/backlit condition did not reduce sample rate, but changed behavior/dispersion

P004 kept an average gaze rate of about 50Hz and had the lowest overall offscreen ratio. This means the slightly dim/backlit condition did not cause obvious tracking failure in this run.

The more interesting signal is behavioral: P004 total reading time is much shorter than P003 for the same participant, and trial 2 has the largest horizontal dispersion among all trial summaries. This could reflect a lighting effect, a second-run familiarity/practice effect, or task strategy change. With the current schema, we cannot separate these causes cleanly.

### 5.3 P002 remains useful as a pressure-test sample

P002 has the lowest sampling rate, about 27.4Hz, while the other three samples are close to 50Hz. This supports the earlier interpretation that glasses plus continuous head movement affects tracking stability more than the P004 dim/backlit lighting condition did in this small set.

### 5.4 Current quality conclusion

All four samples completed the full task and produced usable raw CSV, feature tables, and scanpath visualizations. The current MVP is sufficient for a feasibility demonstration, but not yet sufficient for causal interpretation of gaze differences.

## 6. Methodological implication for next version

The four-sample comparison strengthens the case for adding context and behavior fields before collecting many more samples. At minimum, the next version should record:

1. lighting condition;
2. wearing glasses;
3. head movement / posture instruction;
4. repeated-run order;
5. response timing;
6. calibration quality;
7. mouse, scroll, and AOI context.

Without these fields, P003 vs P004 cannot be interpreted cleanly: the difference could be lighting, familiarity, reading strategy, or participant fatigue.

## 7. Meeting-ready conclusion

> We now have four complete WebGazer pilot samples from two participants/condition sets. The MVP reliably exports gaze/event/probe/quiz data and generates trial-level features plus scanpath visualizations. Glasses plus continuous head movement reduced sampling density most clearly, while the dim/backlit condition did not collapse tracking but may have changed reading behavior and gaze dispersion. The next step should be richer context logging, not model training yet.
