# Eye Tracking Multimodal Data Collection Plan

**日期**: 2026-04-28  
**对应 demo**: `eye_tracking_demo/`  
**状态**: 初版规划文档；已由 `79_next_eye_tracking_data_collection_schema_20260429.md` 进一步细化，暂不改采集页面

## 1. 目标

P001 pilot 证明了 gaze 坐标本身可用，但后续分析不能只依赖 gaze。参照 webcam eye tracking、reading analytics、learning analytics、HCI/TUT probe 类研究，下一版应把 gaze 放进更完整的多模态上下文中。

原则:

- 优先收集低风险、高解释力、可本地记录的信息。
- 不保存视频、截图、人脸图像或诊断身份。
- 所有字段都要能回答一个分析问题，否则不进入第一版。
- 原始事件保留细粒度，后续再聚合成 trial-level features。

## 2. 第一优先级: 必须补的行为与设备上下文

| 类别 | 建议字段 | 为什么重要 | 风险 |
| --- | --- | --- | --- |
| Mouse movement | `mouse_x`, `mouse_y`, `pointer_type`, `buttons`, `event_type=pointer_move/down/up/click` | 鼠标轨迹常能反映阅读定位、犹豫、选项比较；也可与 gaze 对齐判断注意是否在任务区 | 低 |
| Scroll / wheel | `scroll_x`, `scroll_y`, `delta_x`, `delta_y`, `scroll_direction` | 阅读速度、回看、跳读都依赖滚动日志；长文本尤其关键 | 低 |
| Keyboard / focus | `key_event`, `focused_element`, `visibility_state`, `blur/focus` | 判断是否切出页面、是否用键盘操作、任务是否被打断 | 低 |
| Response timing | `probe_show_ms`, `probe_answer_ms`, `quiz_show_ms`, `quiz_answer_ms`, `response_time_ms` | 比只保存答案更有解释力，可分析犹豫、负荷和理解难度 | 低 |
| Viewport / layout | `viewport_width`, `viewport_height`, `device_pixel_ratio`, `screen_width`, `screen_height`, `layout_version` | 解释 gaze 坐标、AOI 映射和不同屏幕的差异；避免坐标不可比 | 低 |
| Stimulus metadata | `text_id`, `text_language`, `text_length_words`, `sentence_count`, `difficulty_level`, `topic`, `question_id` | 后续能控制文本难度、长度、语言和题目差异 | 低 |
| AOI snapshots | `aoi_id`, `aoi_type`, `x`, `y`, `width`, `height`, `visible_from_ms`, `visible_to_ms` | 没有 AOI 就只能看裸坐标，很难解释“看了哪里” | 低 |

## 3. 第二优先级: gaze 质量与校准质量

| 类别 | 建议字段 | 为什么重要 | 风险 |
| --- | --- | --- | --- |
| Gaze sampling | `sample_index`, `sample_interval_ms`, `dropped_sample_count` | 判断采样是否稳定，避免把设备卡顿误读为行为差异 | 低 |
| Validity | `valid_gaze`, `offscreen`, `inside_task_area`, `missing_reason` | 比后处理时猜测更可靠 | 低 |
| Calibration event | `calibration_target_id`, `target_x`, `target_y`, `click_x`, `click_y`, `calibration_round` | 可计算校准点击偏差和重校准需求 | 低 |
| Calibration quality | `calibration_error_px`, `calibration_error_norm`, `quality_flag` | 作为排除或加权标准；很多眼动研究都会报告质量门槛 | 低 |
| WebGazer state | `webgazer_loaded`, `model_version`, `face_mesh_loaded`, `tracking_started_ms` | 方便复现实验和排查失败 | 低 |
| Browser/camera context | `browser`, `os`, `user_agent_hash`, `camera_permission`, `webcam_width`, `webcam_height` | 解释设备差异，但 user agent 建议 hash 或粗粒度保存 | 中低 |

## 4. 第三优先级: 低负担主观与学习状态标签

| 类别 | 建议字段 | 为什么重要 | 风险 |
| --- | --- | --- | --- |
| TUT probe | `probe_tut`, `probe_confidence`, `probe_response_time_ms` | C007/A008 类任务常用；可作为注意状态标签 | 低 |
| Difficulty/familiarity | `difficulty`, `familiarity`, `confidence`, `interest` | 帮助解释 gaze dispersion 和阅读时长 | 低 |
| Fatigue / environment | `fatigue`, `lighting_ok`, `wearing_glasses`, `noise_level` | webcam gaze 对环境敏感；这些字段能解释质量波动 | 中低 |
| Prior knowledge | `prior_knowledge`, `english_reading_comfort` | 对阅读理解和速度影响很大 | 中低 |
| Support preference | `preferred_support`, `need_hint`, `need_slower_pace`, `need_visual_summary` | 与 functional needs 主线一致，比诊断身份更安全 | 中 |

## 5. 暂不建议第一版收集

| 信息 | 原因 |
| --- | --- |
| 原始视频 / 截图 / 人脸图像 | 隐私风险高，当前研究问题不需要 |
| 具体 SEN / neurodivergent 诊断身份 | 伦理和样本风险高，且 MVP 目标是 learning-state / support-needs inference |
| 精确地理位置、账号、姓名、学号 | 与分析问题无关 |
| 长篇开放文本心理状态描述 | 难标准化，隐私负担高 |

## 6. 推荐下一版 CSV 事件结构

继续使用 long-format event log，每一行是一个事件或采样点。新增字段不要都强行填满；不适用时留空。

核心字段:

| 字段 | 说明 |
| --- | --- |
| `participant_id`, `session_id` | 匿名身份与会话 |
| `timestamp_ms`, `event_index` | 时间和顺序 |
| `phase`, `trial_id`, `text_id`, `question_id` | 任务上下文 |
| `event_type`, `event_value` | 事件类型和值 |
| `gaze_x`, `gaze_y`, `valid_gaze`, `offscreen` | gaze 基础信息 |
| `mouse_x`, `mouse_y`, `pointer_type`, `buttons` | 鼠标/触控信息 |
| `scroll_x`, `scroll_y`, `delta_y` | 滚动信息 |
| `aoi_id`, `aoi_type` | 当前或最近 AOI |
| `viewport_width`, `viewport_height`, `device_pixel_ratio` | 坐标解释所需上下文 |
| `response_time_ms` | probe/quiz/按钮响应时间 |
| `calibration_target_id`, `target_x`, `target_y`, `calibration_error_px` | 校准质量 |
| `probe_tut`, `difficulty`, `familiarity`, `confidence`, `fatigue` | 低负担标签 |

## 7. 最小可实施顺序

下一步优先只加 5 类信息，避免一下子把 demo 变重:

1. Mouse/pointer events: move/click/down/up。
2. Scroll/wheel events: scroll position and delta。
3. Response timing: probe/quiz show-to-answer latency。
4. AOI definitions: text panel, probe controls, quiz questions/options, buttons。
5. Calibration quality: target coordinates + click/gaze offset。

这 5 类会显著增加分析空间，同时仍然保持隐私风险低、实现成本可控。

## 8. 组会口径

> 第一轮 pilot 说明 gaze 坐标质量足够好，但后续不能只存 gaze。下一版应同步记录鼠标、滚动、响应时间、AOI、校准质量和设备/viewport 上下文。这样即使 gaze 模型噪声较大，也能通过行为日志和任务上下文解释学习状态，而不是陷入“只有坐标、没有解释变量”的困境。
