# Eye Tracking MVP Pilot Log

**日期**: 2026-04-28  
**Demo URL**: `http://localhost:8765`  
**实现目录**: `eye_tracking_demo/`

## 1. 已完成验证

| 项目 | 状态 | 说明 |
| --- | --- | --- |
| 文件创建 | 完成 | `index.html`, `styles.css`, `app.js`, `README.md`, `analysis/extract_features.py` 已创建 |
| VS Code diagnostics | 通过 | HTML/JS/CSS/Python 未发现编辑器错误 |
| Python 语法检查 | 通过 | `py_compile` 无输出，说明特征脚本语法正常 |
| 本地服务器 | 运行中 | `python -m http.server 8765 -d eye_tracking_demo` |
| 页面打开 | 通过 | 浏览器可打开 `Reading Gaze Pilot` setup 页面 |
| WebGazer 资源路径 | 已修复 | 改为本地固定 WebGazer 3.5.3 + vendored MediaPipe FaceMesh assets，避免请求 `gift-ai.org/eye-track/mediapipe/...` 404 |
| WebGazer 初始化 smoke test | 通过 | 使用浏览器内临时 canvas 假视频流触发 Start，页面进入 `Calibration`，未再出现 `t is not a function` 或 MediaPipe 404 |

## 2. 尚需人工验证

| 项目 | 需要谁 | 原因 |
| --- | --- | --- |
| 摄像头权限 | 用户 | 浏览器需要真实用户点击允许 |
| WebGazer 初始化 | 用户/执行者 | 仍需真实摄像头权限验证 gaze 是否持续输出 |
| 校准质量 | 用户 | 需要真实摄像头、光线和坐姿 |
| CSV 导出 | 用户 | 完成任务后点击 Export CSV |
| 特征提取 | 执行者 | 需要拿到导出的 CSV 后运行 `extract_features.py` |

## 3. 当前试跑步骤

1. 打开 `http://localhost:8765`。
2. 若页面已打开过旧版本，先刷新页面，确保加载的是 `vendor/webgazer-3.5.3.js`。
3. 输入或保留 participant ID。
4. 点击 `Start`。
5. 允许浏览器摄像头权限。
6. 点击 9 个校准点。
7. 读完 3 段文本，每段后回答 probe。
8. 完成 3 道理解题。
9. 点击 `Export CSV`。

## 4. 导出后运行

假设导出文件名为 `reading_gaze_P001_Sxxx.csv`，放到仓库根目录或提供完整路径：

```powershell
c:/Users/Quenton/Documents/Github/nancy-ra/.venv/Scripts/python.exe eye_tracking_demo/analysis/extract_features.py reading_gaze_P001_Sxxx.csv eye_tracking_demo/analysis/features.csv
```

预期输出：

```text
features=3 output=eye_tracking_demo/analysis/features.csv
```

## 5. 初步组会口径

> 我们已经把眼动复现从“读论文计划”推进到普通笔记本 WebGazer MVP：本地页面、校准、阅读任务、TUT probe、理解题、CSV 导出和 Python 特征提取脚本都已准备好。当前还需要真人允许摄像头并完成一次 pilot，以判断校准质量和有效 gaze 比例。

## 6. P001 首轮 pilot 分析

**原始数据**: `eye_tracking_demo/data/raw/reading_gaze_P001_S1777382254070.csv`  
**特征输出**: `eye_tracking_demo/data/processed/features_P001_S1777382254070.csv`

### 6.1 Raw event 摘要

| 指标 | 结果 |
| --- | ---: |
| raw rows | 8525 |
| gaze rows | 8494 |
| calibration clicks | 9 |
| passage shows | 3 |
| probe answers | 3 |
| quiz answers | 3 |
| quiz correct | 3/3 |

事件分布:

| event_type | rows |
| --- | ---: |
| gaze | 8494 |
| phase_start | 9 |
| calibration_click | 9 |
| passage_show | 3 |
| probe_answer | 3 |
| quiz_item_show | 3 |
| quiz_answer | 3 |
| export | 1 |

### 6.2 Trial-level features

| trial_id | gaze_samples | reading_duration_ms | valid_gaze_ratio | offscreen_ratio | gaze_dispersion_x | gaze_dispersion_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 2068 | 41444 | 1.0000 | 0.0058 | 234.98 | 94.61 | 0 | 6 | 2 |
| trial_2 | 1735 | 34377 | 1.0000 | 0.0110 | 249.45 | 58.06 | 0 | 4 | 3 |
| trial_3 | 1750 | 34543 | 1.0000 | 0.0137 | 269.17 | 68.66 | 1 | 4 | 4 |

### 6.3 初步判断

- 这轮 pilot 已经成功跑通从浏览器采集到 CSV、再到 trial-level feature table 的完整闭环。
- `valid_gaze_ratio=1.0` 且 `offscreen_ratio < 0.014`，说明这次 gaze 坐标覆盖质量足够进入后续特征工程。
- 三段 reading trial 都有 probe 标签；trial 3 出现一次 TUT=1，可作为后续窗口特征或可视化检查的第一条正例。
- 当前样本只有 1 人，不做模型效果判断；可以用于证明技术可行性与数据 schema 可用。

## 7. P001 scanpath 可视化

**脚本**: `eye_tracking_demo/analysis/render_scanpaths.py`  
**输出目录**: `eye_tracking_demo/data/visualizations/reading_gaze_P001_S1777382254070/`  
**总览页**: `eye_tracking_demo/data/visualizations/reading_gaze_P001_S1777382254070/index.html`

已生成 8 张 SVG scanpath 图:

1. `scanpath_calibration.svg`
2. `scanpath_reading_trial_1.svg`
3. `scanpath_probe_trial_1.svg`
4. `scanpath_reading_trial_2.svg`
5. `scanpath_probe_trial_2.svg`
6. `scanpath_reading_trial_3.svg`
7. `scanpath_probe_trial_3.svg`
8. `scanpath_quiz.svg`

当前可视化方式:

- 用近似页面背景重建 calibration / reading / probe / quiz 阶段。
- 用蓝到红的 scanpath 表示 gaze 时间顺序。
- 用编号圆点标出抽样 gaze 顺序。
- 用 START / END 标出每个阶段的起止位置。
- 图中显示 samples、duration、offscreen ratio、x/y dispersion 摘要。

## 8. P002 眼镜 + 持续转头 pilot 分析

**原始数据**: `eye_tracking_demo/data/raw/reading_gaze_P002_S1777384531374.csv`  
**特征输出**: `eye_tracking_demo/data/processed/features_P002_S1777384531374.csv`  
**可视化目录**: `eye_tracking_demo/data/visualizations/reading_gaze_P002_S1777384531374/`  
**测试条件**: 参与者戴眼镜，并在录制过程中持续转头，用于观察普通笔记本摄像头追踪的鲁棒性。

### 8.1 Raw event 摘要

| 指标 | P001 | P002 |
| --- | ---: | ---: |
| raw rows | 8525 | 3450 |
| gaze rows | 8494 | 3419 |
| calibration clicks | 9 | 9 |
| passage shows | 3 | 3 |
| probe answers | 3 | 3 |
| quiz answers | 3 | 3 |
| quiz correct | 3/3 | 2/3 |
| overall offscreen ratio | 0.0274 | 0.0140 |
| gaze duration seconds | 169.8 | 124.6 |
| average gaze Hz | 50.0 | 27.4 |

P002 gaze rows by phase:

| phase | gaze rows |
| --- | ---: |
| calibration | 435 |
| reading | 1833 |
| probe | 545 |
| quiz | 606 |

### 8.2 Trial-level features

| trial_id | gaze_samples | reading_duration_ms | valid_gaze_ratio | offscreen_ratio | gaze_dispersion_x | gaze_dispersion_y | TUT | difficulty | familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| trial_1 | 843 | 32364 | 1.0000 | 0.0178 | 302.73 | 100.25 | 0 | 5 | 3 |
| trial_2 | 701 | 26556 | 1.0000 | 0.0000 | 274.01 | 75.57 | 0 | 4 | 4 |
| trial_3 | 834 | 30532 | 1.0000 | 0.0024 | 268.99 | 66.23 | 1 | 7 | 1 |

### 8.3 Scanpath 可视化

已生成 8 张 SVG scanpath 图:

1. `scanpath_calibration.svg`
2. `scanpath_reading_trial_1.svg`
3. `scanpath_probe_trial_1.svg`
4. `scanpath_reading_trial_2.svg`
5. `scanpath_probe_trial_2.svg`
6. `scanpath_reading_trial_3.svg`
7. `scanpath_probe_trial_3.svg`
8. `scanpath_quiz.svg`

浏览器总览页已打开验证，8 张图片均能显示。

### 8.4 初步判断

- P002 在眼镜和持续转头条件下仍然完整跑通，说明当前 MVP 对轻度不稳定姿态不是立即失败。
- P002 的 `valid_gaze_ratio` 仍为 1.0，且整体 offscreen ratio 低于 P001；从坐标落点角度看，这轮数据仍可分析。
- 主要质量下降体现在采样密度：P002 平均 gaze rate 约 27.4Hz，低于 P001 的约 50.0Hz；这可能来自持续转头、摄像头追踪不稳定、或本轮任务总时长较短。
- P002 trial 1 的横向 dispersion 明显高于 P001 trial 1，符合持续转头可能带来更大水平偏移的预期。
- 这轮可以作为“非理想摄像头姿态压力测试”样本，但后续正式 pilot 应记录眼镜、光线、转头/坐姿等上下文字段，否则很难解释采样率和 dispersion 差异。

## 9. P003/P004 与四样本比较

**详细报告**: `docs/72_eye_tracking_four_sample_comparison_20260428.md`

新增样本:

| sample | 条件 | raw file | feature file | scanpath index |
| --- | --- | --- | --- | --- |
| P003 | 受试者 2；不戴眼镜；光条件与 P001/P002 相同；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P003_S1777385935863.csv` | `eye_tracking_demo/data/processed/features_P003_S1777385935863.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P003_S1777385935863/index.html` |
| P004 | 受试者 2；不戴眼镜；关闭台灯，略暗光、略逆光；尽量不转头，只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P004_S1777386312284.csv` | `eye_tracking_demo/data/processed/features_P004_S1777386312284.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P004_S1777386312284/index.html` |

### 9.1 四样本 raw-level 对比

| sample | raw rows | gaze rows | duration_s | avg_hz | offscreen_all | reading_gaze | quiz_correct |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P001 | 8525 | 8494 | 169.8 | 50.0 | 0.0274 | 4080 | 3/3 |
| P002 | 3450 | 3419 | 124.6 | 27.4 | 0.0140 | 1833 | 2/3 |
| P003 | 12946 | 12915 | 260.1 | 49.6 | 0.0132 | 5108 | 2/3 |
| P004 | 6256 | 6225 | 124.6 | 50.0 | 0.0050 | 3982 | 2/3 |

### 9.2 四样本 trial-level 平均对比

| sample | total reading s | mean gaze samples/trial | mean offscreen | mean disp x | mean disp y | TUT positive | mean difficulty | mean familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P001 | 110.4 | 1851.0 | 0.0102 | 251.2 | 73.8 | 1/3 | 4.7 | 3.0 |
| P002 | 89.5 | 792.7 | 0.0067 | 281.9 | 80.7 | 1/3 | 5.3 | 2.7 |
| P003 | 168.9 | 2775.7 | 0.0059 | 271.8 | 98.5 | 3/3 | 4.7 | 2.3 |
| P004 | 97.2 | 1635.7 | 0.0053 | 306.2 | 93.8 | 3/3 | 3.7 | 4.0 |

### 9.3 四样本初步结论

- P003 是当前数据量最大的样本，平均采样率接近 50Hz，说明在受试者 2 不戴眼镜、尽量不转头的正常光照条件下，MVP 可以持续稳定采样。
- P004 在略暗光、略逆光下仍保持约 50Hz，且 overall offscreen ratio 最低；这轮没有出现明显追踪崩溃。
- P004 相比 P003 阅读时间明显缩短，且 trial 2 的横向 dispersion 达到 349.5，是四个样本 trial 摘要中最高的；这可能来自暗光/逆光、第二次重复任务的熟悉效应、阅读策略变化或疲劳，当前 schema 不能区分。
- P002 的平均采样率最低，约 27.4Hz；在这四个样本里，戴眼镜并持续转头比 P004 的略暗逆光更明显地影响采样密度。
- 四个样本都完成了 raw CSV、feature table 和 8 张 scanpath SVG，当前 MVP 足够支撑组会中的 feasibility demo；下一版重点应转向记录光照、眼镜、转头/坐姿、重复顺序、响应时间、校准质量、鼠标/滚动/AOI 等上下文。

## 10. P005 严格正常条件样本与五样本更新

**详细报告**: `docs/73_eye_tracking_five_sample_comparison_20260428.md`

P005 是受试者 1 的最严格正常条件样本：不戴眼镜，正常光照，尽量避免上下左右转头，尽量只动瞳孔。

| sample | 条件 | raw file | feature file | scanpath index |
| --- | --- | --- | --- | --- |
| P005 | 受试者 1；不戴眼镜；正常光照；最严格避免转头，尽量只动瞳孔 | `eye_tracking_demo/data/raw/reading_gaze_P005_S1777388229181.csv` | `eye_tracking_demo/data/processed/features_P005_S1777388229181.csv` | `eye_tracking_demo/data/visualizations/reading_gaze_P005_S1777388229181/index.html` |

### 10.1 五样本 raw-level 对比

| sample | raw rows | gaze rows | duration_s | avg_hz | offscreen_all | reading_gaze | quiz_correct |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | --- |
| P001 | 8525 | 8494 | 169.8 | 50.0 | 0.0274 | 4080 | 3/3 |
| P002 | 3450 | 3419 | 124.6 | 27.4 | 0.0140 | 1833 | 2/3 |
| P003 | 12946 | 12915 | 260.1 | 49.6 | 0.0132 | 5108 | 2/3 |
| P004 | 6256 | 6225 | 124.6 | 50.0 | 0.0050 | 3982 | 2/3 |
| P005 | 5645 | 5614 | 118.0 | 47.6 | 0.0082 | 3586 | 3/3 |

### 10.2 五样本 trial-level 平均对比

| sample | total reading s | mean gaze samples/trial | mean offscreen | mean disp x | mean disp y | TUT positive | mean difficulty | mean familiarity |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| P001 | 110.4 | 1851.0 | 0.0102 | 251.2 | 73.8 | 1/3 | 4.7 | 3.0 |
| P002 | 89.5 | 792.7 | 0.0067 | 281.9 | 80.7 | 1/3 | 5.3 | 2.7 |
| P003 | 168.9 | 2775.7 | 0.0059 | 271.8 | 98.5 | 3/3 | 4.7 | 2.3 |
| P004 | 97.2 | 1635.7 | 0.0053 | 306.2 | 93.8 | 3/3 | 3.7 | 4.0 |
| P005 | 86.4 | 1352.7 | 0.0033 | 252.1 | 75.1 | 0/3 | 4.0 | 4.0 |

### 10.3 P005 初步判断

- P005 是目前受试者 1 最干净的严格条件基线：不戴眼镜、不刻意转头、正常光照，quiz 3/3，TUT 为 0/3。
- P005 平均采样率为 47.6Hz，明显高于 P002 的 27.4Hz，支持“眼镜 + 持续转头会降低采样密度”的判断。
- P005 的 mean offscreen ratio 为 0.0033，是五个样本 trial-level 平均里最低的；说明严格正常条件下 gaze 坐标稳定性较好。
- P005 的阅读总时长为 86.4 秒，比 P001 更短，说明它是一个更快但更干净的基线，而不是数据量最大的样本。
- 五个样本中，除 P002 外，其余四个都接近 48-50Hz；当前 MVP 可以支撑小规模 feasibility pilot，但下一版必须把实验条件直接写入 CSV。
