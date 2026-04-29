# 组会后下一阶段任务计划

**日期**: 2026-04-29  
**来源**: 2026-04-29 组会纪要与会后讨论  
**面向节点**: 下一次组会前，暂按 5 月 22 日 19:00 准备  
**核心目标**: 把当前 WebGazer demo 从 feasibility demo 推进为可执行的 Stage 1 数据收集与论文方案。

## 1. 会后方向判断

这次组会对项目是正向推进。导师组没有否定 browser-based webcam eye tracking 路线，而是把重点从“demo 能不能跑”推进到“如何设计成可发表的分阶段研究”。

会后项目定位应从：

> 我们做了一个 WebGazer 眼动 demo，看能不能用于 SEN/SEND 支持。

调整为：

> 我们先用低成本 web-based sensing 识别在线学习任务中的行为模式，尤其是高困惑、高负荷、注意波动和支持需求相关模式；之后再研究这些模式如何迁移到不同学习者需求和个性化支持。

第一阶段不做 SEN/SEND 身份诊断，也不做完整 adaptive AI 系统。第一阶段先验证低成本浏览器过程数据是否能产生可解释、可复现、可发表的 learning state patterns。

## 2. 第一阶段推荐研究问题

建议下一阶段统一使用这个研究问题作为主线：

> Can low-cost browser-based gaze and interaction logs reveal task-induced learning state patterns in online learning?

中文表述：

> 普通笔记本浏览器中的眼动、鼠标、滚动、答题时间和自评数据，能否识别由任务诱发的高困惑、高负荷、注意波动和支持需求模式？

这个表述的好处：

1. 不把学生身份作为分类目标。
2. 把任务操控放在中心，而不是把差异归因于个人特质。
3. 允许 gaze 不稳定时降级为辅助信号。
4. 第一阶段结果可以独立形成 learning analytics / educational technology paper。

## 3. 优先级总览

| 优先级 | 任务 | 目的 | 建议完成时间 |
| --- | --- | --- | --- |
| P0 | 会后路线确认邮件 | 和 CHEN、Jie 锁定方向，避免理解偏差 | 1 天内 |
| P0 | demo 后台自动保存 | 支撑 Prolific / 大样本数据收集 | 3-5 天 |
| P0 | 补全行为过程字段 | 从单纯 gaze demo 变成多通道 process sensing | 3-5 天 |
| P0 | Stage 1 研究问题定稿 | 把工程 demo 转成可发表研究命题 | 1-2 天 |
| P0 | 第一版任务操控收窄 | 避免实验设计过度复杂 | 2-3 天 |
| P1 | 题库与任务材料 shortlist | 避免从零设计题目 | 3-5 天 |
| P1 | Prolific 分阶段招募方案 | 准备第一阶段大样本路线 | 2-3 天 |
| P1 | 第一篇 paper outline | 提前对齐论文贡献 | 1-2 天 |
| P1 | 更新 data collection protocol | 形成正式执行协议 | 2-4 天 |
| P2 | 个性化界面/active support 完整系统 | 后续阶段使用，不抢第一阶段时间 | 延后 |
| P2 | 复杂学习者类型分类 | 等数据稳定后再讨论 | 延后 |
| P2 | blink/心理状态自动判断 | 当前数据不支持可靠推断 | 延后 |

## 4. P0 任务细化

### 4.1 会后路线确认邮件

**目标**: 用一封简短 follow-up email 确认会后理解。

建议邮件重点：

1. Stage 1 聚焦 browser-based process data 和 task-induced learning states。
2. 不做 SEN/SEND 身份诊断。
3. 先验证 webcam gaze + interaction logs + self-report 是否能识别高困惑、高负荷、注意波动和支持需求相关模式。
4. 后续再做 SEN/SEND transfer check、support mapping 和 personalized support。
5. 下一步技术任务是自动保存数据和丰富行为字段。

建议句子：

> My understanding is that Stage 1 should focus on low-cost browser-based process sensing for task-induced learning states, rather than diagnostic classification of SEN/SEND learners. If Stage 1 shows stable behavioral patterns, we can then examine transfer to learners with diverse support needs and design targeted support interventions.

### 4.2 demo 后台自动保存

**目标**: 从手动导出 CSV 变成可用于远程实验的数据采集系统。

最低可用版本：

1. 自动生成或接收 `participant_id` / `session_id`。
2. 前端自动 POST raw event log 到后台。
3. 后台保存为 CSV 或 JSONL。
4. 完成任务后显示 Prolific completion code。
5. 保留手动 export 作为 backup。
6. 记录任务版本和题目版本，避免不同版本数据混在一起。

建议第一版不要上复杂数据库。可先用本地/服务器端文件保存：

```text
server_data/
  raw/
    participant_session_timestamp.jsonl
  metadata/
    participant_session_metadata.json
```

后续需要部署时，再考虑数据库或云存储。

### 4.3 补全下一版行为过程字段

当前 demo 主要记录：`timestamp_ms`, `phase`, `trial_id`, `gaze_x/y`, `event_type`, `probe`, `quiz`。

下一版优先增加：

| 字段组 | 字段例子 | 用途 |
| --- | --- | --- |
| 鼠标/指针 | `pointer_move`, `mouse_x/y`, `click`, `pointer_down/up` | 判断辅助阅读、犹豫、选择行为 |
| 滚动 | `scroll_y`, `delta_y`, `scroll_direction` | 判断跳读、回看、停留位置 |
| 反应时间 | `stimulus_onset_ms`, `response_latency_ms`, `answer_changed` | 判断犹豫、负荷和自我修正 |
| AOI | `aoi_id`, `aoi_type`, `aoi_rect` | 把 gaze/pointer 转成“看哪里/指哪里” |
| 设备上下文 | `browser`, `screen`, `viewport`, `device_pixel_ratio` | 解释数据质量差异 |
| 眼动质量 | `valid_gaze`, `offscreen`, `calibration_error_px` | 避免把坏数据当行为差异 |
| 实验上下文 | `lighting_condition`, `wearing_glasses`, `head_movement` | 解释 gaze 可靠性 |
| 主观标签 | `difficulty`, `confusion`, `fatigue`, `tech_trust`, `support_preference` | 给过程数据提供解释标签 |

当前不建议优先做 blink。当前没有保存视频、眼睑、瞳孔或 FaceMesh landmarks，blink 只能从 gaze 中断间接猜测，容易和头动、丢脸、眼镜反光混淆。

### 4.4 Stage 1 任务操控收窄

Jie 提到可以操控内容、格式、时间安排、学习次序和 active support，但第一版不能全部放进去。

建议第一阶段只保留 2-3 个变量：

| 变量 | 简单版本 | 暂不加入的复杂版本 |
| --- | --- | --- |
| 难度 | easy / hard | 多级课程结构、长期学习路径 |
| 支持 | no support / hint or glossary | 完整 adaptive support system |
| 格式 | plain text / supported text | 文本、图像、声音、多媒体全组合 |

一个可执行的第一版设计：

| 条件 | 内容 | 支持 | 目标 |
| --- | --- | --- | --- |
| A | easy text | no support | baseline |
| B | hard text | no support | 诱发高负荷/困惑 |
| C | hard text | glossary or hint | 检查支持是否改变行为模式 |

如果时间不足，先做 A/B 两条件，支持工具留到第二个 pilot。

## 5. P1 任务细化

### 5.1 题库与任务材料 shortlist

会议明确建议不要从零设计题目。下一步需要找现成任务材料或可改造题库。

优先找三类：

1. reading comprehension / text reasoning。
2. non-verbal reasoning / pattern reasoning。
3. cognitive load 或 difficulty manipulation 的 online learning task。

输出建议做成一张表：

| 来源 | 题型 | 是否公开可用 | 难度分级 | 是否适合 Prolific | 是否适合 AOI/眼动分析 | 备注 |
| --- | --- | --- | --- | --- | --- | --- |
| 待填 | reading comprehension | 待查 | 待查 | 待查 | 待查 | 待查 |
| 待填 | non-verbal reasoning | 待查 | 待查 | 待查 | 待查 | 待查 |

检索关键词建议：

```text
online reading comprehension item bank difficulty levels
text reasoning task cognitive load online learning
non-verbal reasoning matrix task open dataset
learning analytics reading comprehension gaze mouse scroll response time
Prolific online learning experiment reading comprehension task
```

### 5.2 Prolific 分阶段招募方案

不要一开始承诺 1000 人。建议分阶段：

| 阶段 | 样本量 | 目的 |
| --- | ---: | --- |
| internal pilot | 5-10 | 验证流程、字段、后台保存 |
| Prolific smoke test | 30-50 | 验证远程流程、completion code、数据质量 |
| Stage 1 main study | 100-200 | 第一篇 paper 的核心数据 |
| extended sample | 500-1000 | 前面信号稳定后再扩大，研究 pattern diversity |

Prolific 准备事项：

1. inclusion/exclusion criteria。
2. consent statement。
3. payment estimate。
4. expected completion time。
5. completion code。
6. attention check。
7. duplicate participation prevention。
8. privacy wording: 不保存视频、人脸图像或诊断身份。

### 5.3 第一篇 paper outline

暂定题目：

> Low-cost browser-based process sensing for detecting task-induced learning state patterns

建议结构：

1. **Motivation**: iTrack 设备受经费限制，低成本 web sensing 有必要。
2. **Gap**: WebGazer、learning analytics、SEN/SEND support 各自存在，但尚未在低成本在线学习过程感知中系统连接。
3. **Research question**: 过程数据能否反映 task-induced learning states。
4. **Method**: browser demo + task manipulation + Prolific data。
5. **Measures**: gaze, mouse, scroll, response latency, probe, quiz, support preference。
6. **Analysis**: 数据质量、特征与 probe/表现关系、行为模式聚类或分类。
7. **Contribution**: 低成本、可扩展、非诊断式的 learning process sensing。

### 5.4 更新 data collection protocol

需要把 demo schema、会议决策和伦理边界合并成正式执行协议。

协议必须写清：

1. 不保存视频、截图、人脸图像。
2. 哪些字段自动记录。
3. 哪些字段来自学生自评。
4. 哪些字段由研究者手动记录。
5. gaze 不稳定时如何降级。
6. 如何处理 Prolific participant id 和 completion code。
7. 如何保存、命名、备份数据。

## 6. P2 暂缓任务

### 6.1 完整个性化界面和 active support 系统

现在只需要最小支持入口，例如 glossary 或 hint。不要急着做完整 adaptive AI interface。完整系统应放在 Stage 3。

### 6.2 复杂学习者类型分类

暂时不要使用“诊断分组”口径。建议只说：

> behavioral pattern grouping

等 Stage 1 数据稳定后，再讨论 cluster/profile。

### 6.3 blink、头动和心理状态自动判断

当前版本不支持可靠 blink 推断。头动可以先用结构化人工记录，心理状态必须由 probe/问卷辅助验证，不能只靠 gaze 推断。

## 7. 推荐执行顺序

| 时间 | 任务 | 输出 |
| --- | --- | --- |
| 今天/明天 | 会后确认邮件 | 发给 CHEN 和 Jie 的方向确认 |
| 第 1-3 天 | 后台自动保存原型 | 可 POST 并保存 raw event log |
| 第 2-5 天 | 补鼠标、滚动、点击、latency、AOI、设备字段 | 新版 raw schema |
| 第 3-7 天 | 题库检索 | 题库/任务材料 shortlist |
| 第 5-8 天 | 任务操控定稿 | easy/hard/support 条件设计 |
| 第 7-10 天 | internal pilot | 5-10 人数据和 bug list |
| 第 10-14 天 | 初步 feature extraction 和质量报告 | 采样率、valid、offscreen、latency、mouse/scroll summary |
| 第 14 天后 | Prolific smoke test 准备 | consent、completion code、30-50 人方案 |
| 组会前 2-3 天 | 汇报材料整理 | demo、protocol、题库表、pilot 结果、paper outline |

## 8. 下一次组会建议展示内容

下一次组会最好不要只展示 PPT，而是展示 5 个具体产物：

1. **新版 demo**: 能自动保存数据。
2. **数据流图**: 浏览器事件如何进入后台数据文件。
3. **字段表**: gaze、mouse、scroll、latency、probe、quiz、context。
4. **任务设计表**: easy/hard、support/no support、文本/非文本。
5. **小 pilot 结果**: 即使只有 5-10 人，也展示数据质量和几个初步 feature。

## 9. 当前最重要的一句话

下一阶段优先级应收束为：

> 先把 demo 工程化到能自动收 Prolific 数据，再把 Stage 1 研究问题和任务操控收窄到可以发表的程度。

当前不应优先做：

> 完整自适应系统、复杂分类模型、SEN/SEND 诊断式分组、blink 或心理状态自动判断。
