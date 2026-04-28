# 普通笔记本眼动最小复现 Playbook

**日期**: 2026-04-28  
**对应总计划**: `61_next_meeting_dual_deliverable_plan_20260428.md`  
**目的**: 基于 webcam-based eye tracking / WebGazer 相关论文，构建普通笔记本可运行的学习状态采集与分析最小闭环。

## 1. 复现定位

本轮目标是 **feasibility replication / method-inspired reproduction**，不是严格逐参数复现，也不是诊断分类系统。

推荐目标:

- 采集在线阅读任务中的 gaze 坐标、任务事件、probe 回答和理解题结果。
- 提取学习状态相关特征: gaze dispersion、离屏比例、阅读时间、回答时间。
- 初步分析这些特征是否随 task-unrelated thought (TUT)、文本熟悉度、理解表现变化。

暂不承诺:

- 不诊断 neurodivergent / SEN 学生。
- 不承诺达到原论文 AUROC 或准确率。
- 不保存原始视频或人脸图像。

## 2. 核心论文源

| ID | 标题 | 年份 | 当前状态 | 本轮用途 |
| --- | --- | ---: | --- | --- |
| A007 | Using a Webcam Based Eye-tracker to Understand Students' Thought Patterns and Reading Behaviors in Neurodivergent Classrooms | 2023 | 摘要与方法卡已有；ACM 页面 403；本地无全文 | 小样本课堂/阅读任务 + thought pattern probe 设计 |
| C007 | Using Webcam-Based Eye Tracking during a Learning Task to Understand Neurodivergence | 2025 | EDM 页面可读；方法细节已进入 source pack | WebGazer + N=354 + 性能边界 + 伦理边界主模板 |
| A008 | One Size Does Not Fit All: Considerations when using Webcam-Based Eye Tracking to Models of Neurodivergent Learners' Attention and Comprehension | 2025 | 摘要与方法卡已有；ACM 页面 403；本地无全文 | TUT / comprehension 建模与公平性警示 |

Source pack: `67_eye_tracking_source_pack_20260428.md`。

## 3. 分层复现范围

### Level 0: 证据复现

目标: 补全文和方法细节，确认每篇文章实际做了什么。

输出: 核心文献方法卡，含任务、样本、输入信号、标签、模型、指标、边界。

当前状态: C007 已达到可执行级别；A007/A008 仍需用户通过机构访问下载 ACM 全文。

### Level 1: 管道复现

目标: 在本机浏览器中跑通 webcam gaze 采集、阅读任务、probe 和数据导出。

输出: `eye_tracking_demo/`。

当前状态: 已创建 WebGazer MVP，并通过页面加载检查；摄像头采集需用户授权试跑。

### Level 2: 功能性指标复现

目标: 从 gaze + 行为数据中提取基础特征，预测或解释 TUT、理解题、文本熟悉度、阅读困难等非诊断指标。

输出: `eye_tracking_demo/analysis/extract_features.py` 与 pilot log。

当前状态: 特征提取脚本已创建并通过语法检查；等待真实导出 CSV。

### Level 3: 身份/群体差异研究

本阶段不做。只有在伦理、样本、导师批准和明确知情同意都到位后，才考虑从功能状态扩展到群体差异。

## 4. MVP 任务流程

1. Setup: 输入匿名 participant ID。
2. Camera/WebGazer: 用户点击 Start 并允许摄像头。
3. Calibration: 9 点点击校准。
4. Reading: 3 段短文本。
5. Probe: 每段后记录 TUT、难度、熟悉度。
6. Quiz: 3 道理解题。
7. Export: 本地导出 CSV。
8. Feature extraction: 用 Python 脚本生成 trial-level features。

## 5. 数据字段

### Raw gaze / event CSV

| 字段 | 说明 |
| --- | --- |
| `participant_id` | 匿名 ID |
| `session_id` | 会话 ID |
| `timestamp_ms` | 浏览器相对时间戳 |
| `phase` | setup / calibration / reading / probe / quiz / done |
| `trial_id` | 阅读 trial 或 quiz |
| `gaze_x`, `gaze_y` | WebGazer 预测坐标 |
| `page_width`, `page_height` | 页面尺寸 |
| `event_type` | gaze / phase_start / calibration_click / probe_answer / quiz_answer / export |
| `event_value` | 事件值 |
| `text_id` | 阅读文本 ID |
| `probe_tut` | TUT probe 回答 |
| `difficulty` | 难度自评 |
| `familiarity` | 熟悉度自评 |
| `comprehension_correct` | 理解题是否正确 |

### Feature CSV

| 字段 | 说明 |
| --- | --- |
| `trial_id` | 阅读 trial |
| `gaze_samples` | gaze 采样点数 |
| `reading_duration_ms` | trial 内 gaze 时间跨度 |
| `valid_gaze_ratio` | 有效 gaze 比例 |
| `offscreen_ratio` | 坐标越界比例 |
| `gaze_dispersion_x`, `gaze_dispersion_y` | x/y 离散度 |
| `probe_tut` | TUT 标签 |
| `difficulty` | 难度标签 |
| `familiarity` | 熟悉度标签 |

## 6. 伦理边界

本轮 MVP 默认规则:

- 不保存视频。
- 不保存截图。
- 不做人脸识别。
- 不输出诊断标签。
- participant ID 使用匿名编号。
- 数据默认保存在本地，由用户手动导出。

## 7. 用户协助点

| 协助点 | 说明 |
| --- | --- |
| 下载 ACM 全文 | A007/A008 需要机构访问 |
| 摄像头权限测试 | 浏览器必须由真实用户允许摄像头访问 |
| 完成一次 pilot | 需要真实 gaze CSV 才能验证特征提取 |
| 确认阅读材料语言 | 当前 MVP 是英文短文本；后续可换成中文或课程材料 |

## 8. 当前输出

| 文件 | 状态 |
| --- | --- |
| `67_eye_tracking_source_pack_20260428.md` | 已完成 |
| `68_eye_tracking_demo_design_20260428.md` | 已完成 |
| `69_eye_tracking_mvp_pilot_log_20260428.md` | 已完成 |
| `eye_tracking_demo/index.html` | 已完成 |
| `eye_tracking_demo/app.js` | 已完成 |
| `eye_tracking_demo/styles.css` | 已完成 |
| `eye_tracking_demo/analysis/extract_features.py` | 已完成 |

## 9. 当前 GO 条件

已满足:

- C007 方法参数已可复用。
- 第一版不做身份诊断，只做功能性学习状态。
- WebGazer MVP 已创建。
- 本地服务器页面已打开。

下一步 GO 条件:

- 用户完成一次浏览器摄像头试跑并导出 CSV。
- 用导出 CSV 运行 `extract_features.py`，得到 feature table。
