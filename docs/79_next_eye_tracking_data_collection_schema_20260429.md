# 下一版眼动与交互数据采集计划

**日期**: 2026-04-29  
**对应 demo**: `eye_tracking_demo/`  
**上游依据**: `70_eye_tracking_multimodal_data_collection_plan_20260428.md`, `77_next_meeting_literature_evidence_table_20260429.md`, `78_next_meeting_brief_20260429.md`  
**目的**: 明确下一版应该收集哪些低风险、高价值数据，以及哪些数据只作为远程实验辅助材料。

## 1. 核心原则

下一版数据采集的目标不是扩大隐私范围，而是补齐解释 gaze 所需的行为上下文。

原则如下：

1. 不在网页端保存原始视频、人脸图像或截图。
2. 不采集具体诊断身份，不让系统判断学生属于哪一类人。
3. 优先采集低风险、高解释力、可本地 CSV 记录的信息。
4. 主数据表记录任务过程和行为上下文；Zoom 录制如果需要，应作为独立辅助材料，单独同意、单独保存、单独编号。
5. 所有字段都要能回答一个分析问题，否则不进入第一版实现。

## 2. 第一优先级：低风险高价值行为信息

| 优先级 | 类别 | 事件/字段 | 分析价值 | 风险 |
| ---: | --- | --- | --- | --- |
| 1 | 鼠标 / pointer | `pointer_move`, `pointer_down`, `pointer_up`, `click`, `mouse_x`, `mouse_y`, `pointer_type`, `buttons`, `button` | 反映阅读定位、犹豫、选项比较、是否用鼠标辅助阅读；可与 gaze 对齐判断注意是否在任务区。 | 低 |
| 2 | 滚动 / wheel | `scroll`, `wheel`, `scroll_x`, `scroll_y`, `delta_x`, `delta_y`, `scroll_direction`, `scroll_velocity` | 解释阅读速度、回看、跳读、是否停留在某段文本；长文本任务尤其关键。 | 低 |
| 3 | 响应时间 | `probe_show_ms`, `probe_answer_ms`, `quiz_show_ms`, `quiz_answer_ms`, `response_latency_ms` | 比只保存答案更有解释力，可分析犹豫、负荷、理解难度和 self-regulated learning。 | 低 |
| 4 | AOI 区域 | `aoi_id`, `aoi_type`, `aoi_x`, `aoi_y`, `aoi_width`, `aoi_height`, `visible_from_ms`, `visible_to_ms` | 把裸 gaze 坐标转化为“看了文本、题目、选项还是按钮”。 | 低 |
| 5 | 校准质量 | `calibration_target_id`, `target_x`, `target_y`, `click_x`, `click_y`, `gaze_x_at_click`, `gaze_y_at_click`, `calibration_error_px`, `quality_flag` | 判断每轮 tracking 是否可信，形成排除/加权标准。 | 低 |

## 3. 第二层信息：质量、设备和环境上下文

| 类别 | 建议字段 | 为什么值得收 |
| --- | --- | --- |
| 采样稳定性 | `sample_index`, `sample_interval_ms`, `effective_hz`, `dropped_sample_count`, `long_gap_count` | 避免把设备卡顿或浏览器掉帧误读为阅读行为差异。 |
| gaze 有效性 | `valid_gaze`, `offscreen`, `inside_task_area`, `missing_reason` | 后处理不用再猜测样本是否可用。 |
| viewport / layout | `viewport_width`, `viewport_height`, `device_pixel_ratio`, `screen_width`, `screen_height`, `layout_version` | gaze 坐标、AOI 和不同设备之间的可比性依赖这些字段。 |
| 浏览器/摄像头上下文 | `browser_family`, `os_family`, `user_agent_hash`, `camera_permission`, `webcam_width`, `webcam_height` | 解释不同设备和权限状态导致的质量差异；避免保存完整 user agent。 |
| 页面状态 | `visibility_state`, `window_focus`, `blur_ms`, `focus_ms`, `fullscreen_state` | 判断远程实验中是否切屏、窗口是否被遮挡或任务是否中断。 |
| 任务材料元数据 | `text_id`, `text_length_words`, `sentence_count`, `topic`, `difficulty_level`, `question_id`, `option_id` | 控制文本长度、难度、主题和题目差异。 |
| 主观状态 | `fatigue`, `lighting_condition`, `wearing_glasses`, `head_movement_instruction`, `posture_note`, `familiarity`, `confidence` | 解释 P002/P004/P005 这类条件差异。 |
| 支持偏好 | `need_hint`, `need_more_time`, `need_visual_summary`, `preferred_support`, `support_confidence` | 与 functional support needs 主线一致，比诊断身份更安全。 |

## 4. 从文献启发来的补充字段

| 来源 | 启发 | 可收集字段 |
| --- | --- | --- |
| A4: SEND students and e-authentication | 数据化系统必须避免误判和惩罚性使用，且要关注学生对技术可靠性的感受。 | `tech_trust_rating`, `privacy_comfort`, `perceived_intrusiveness`, `system_error_reported`, `participant_comment_optional` |
| A7: process data and self-regulated learning | 学习过程数据可以揭示最终分数看不到的 regulation 差异。 | `review_count`, `backtrack_count`, `answer_change_count`, `time_before_first_action_ms`, `idle_period_count` |
| A1/B1: assistive/adaptive technologies | 支持工具要匹配实际需求，而不是默认一种支持适合所有人。 | `support_option_shown`, `support_option_used`, `support_helpful_rating`, `support_type` |
| A3: accessible university systems | 困难可能来自系统和任务设计，不只来自学生个人。 | `layout_issue_reported`, `instruction_clarity`, `access_barrier_note`, `needed_researcher_help` |
| A6: sensor/process data rationale | 传感器数据应服务实时支持和事后解释。 | `real_time_flag_candidate`, `quality_flag`, `support_trigger_reason` |

## 5. 远程 Zoom 实验的辅助材料

远程通过 Zoom 帮助受试者完成实验时，可以考虑录制视频和音频，但它应当作为**独立辅助材料**，而不是网页主数据的一部分。

### 5.1 可以记录什么

| 类别 | 建议记录 | 用途 |
| --- | --- | --- |
| Zoom 录制 | 屏幕共享、实验过程音频、研究者提示、受试者口头反馈 | 事后检查任务是否被打断、是否有研究者干预、是否出现设备/理解问题。 |
| 录制元数据 | `zoom_recording_id`, `recording_start_wall_time`, `recording_end_wall_time`, `consent_for_recording` | 方便和 CSV 对齐，同时保留同意记录。 |
| 研究者干预日志 | `researcher_help_event`, `help_type`, `help_timestamp_ms`, `help_note` | 区分自然行为和被研究者提示后的行为。 |
| 远程技术问题 | `zoom_audio_issue`, `screen_share_issue`, `network_issue`, `camera_setup_issue` | 解释异常延迟、暂停和数据质量下降。 |

### 5.2 风险控制

1. Zoom 录制前必须单独说明并获得同意。
2. 录制文件不要和匿名 CSV 混在同一个公开分析包里。
3. 汇报和论文中尽量使用事件摘要，不直接展示人脸或声音。
4. 如果只需要回看研究者是否干预，优先保留 intervention log，而不是长期保留完整音视频。

## 6. 我建议额外收集的数据

除用户提出的五类核心信息外，我建议补充以下几类，优先级从高到低排列。

| 优先级 | 额外数据 | 原因 |
| ---: | --- | --- |
| 1 | 页面可见性与焦点状态 | 远程实验很容易切屏、弹窗或 Zoom 遮挡；没有 focus/visibility 会误读停顿。 |
| 2 | researcher intervention log | Zoom 辅助下，研究者提示会显著影响行为数据；必须知道什么时候发生了帮助。 |
| 3 | idle / hesitation segments | 长时间没有鼠标、滚动、gaze 移动可能是认真阅读、卡住、分心或技术问题，需要标记。 |
| 4 | answer changes | quiz/probe 选项是否改过，可以反映犹豫和不确定性。 |
| 5 | support preference / helpfulness | 与 functional support needs 直接相关，也能避免诊断身份采集。 |
| 6 | instruction clarity and task confusion | 如果学生没理解任务，gaze 数据再好也不代表学习状态。 |
| 7 | app/schema version | 工程上必须知道数据来自哪一版页面和字段，否则后续合并会混乱。 |
| 8 | event loss / logging errors | 如果浏览器性能或 JS error 影响采集，分析阶段要能发现。 |

## 7. 推荐 CSV 事件结构

继续使用 long-format event log。每一行代表一个 gaze sample、pointer event、scroll event、task event、AOI snapshot 或 researcher/Zoom metadata event。

| 字段组 | 字段 |
| --- | --- |
| identity/session | `participant_id`, `session_id`, `run_order`, `schema_version`, `app_version` |
| time/order | `timestamp_ms`, `wall_time_iso`, `event_index`, `phase`, `trial_id` |
| event | `event_type`, `event_value`, `event_source` |
| gaze | `gaze_x`, `gaze_y`, `valid_gaze`, `offscreen`, `inside_task_area`, `sample_interval_ms` |
| pointer | `mouse_x`, `mouse_y`, `pointer_type`, `buttons`, `button` |
| scroll | `scroll_x`, `scroll_y`, `delta_x`, `delta_y`, `scroll_direction` |
| AOI | `aoi_id`, `aoi_type`, `aoi_x`, `aoi_y`, `aoi_width`, `aoi_height` |
| response | `question_id`, `option_id`, `response_latency_ms`, `answer_changed`, `confidence` |
| calibration | `calibration_target_id`, `target_x`, `target_y`, `click_x`, `click_y`, `calibration_error_px`, `quality_flag` |
| environment | `lighting_condition`, `wearing_glasses`, `head_movement_instruction`, `posture_note`, `fatigue` |
| browser/device | `viewport_width`, `viewport_height`, `device_pixel_ratio`, `browser_family`, `os_family`, `webcam_width`, `webcam_height` |
| remote/Zoom | `zoom_recording_id`, `consent_for_recording`, `researcher_help_event`, `help_type`, `network_issue` |
| support needs | `preferred_support`, `support_option_used`, `support_helpful_rating`, `need_more_time`, `need_visual_summary` |

## 8. 最小实现顺序

### 第 1 批：必须实现

1. pointer/mouse events;
2. scroll/wheel events;
3. probe/quiz response latency;
4. AOI snapshots;
5. calibration quality。

### 第 2 批：强烈建议

1. lighting/glasses/head movement/posture/fatigue;
2. viewport/devicePixelRatio/browser/camera context;
3. sampling stability and valid gaze flags;
4. page visibility/focus;
5. researcher intervention log for Zoom sessions。

### 第 3 批：pilot 后再决定

1. support preference and helpfulness;
2. optional participant comment;
3. answer change and idle segment derived features;
4. Zoom audio/video coding scheme。

## 9. 组会口径

> 下一版不是为了收更多敏感信息，而是为了让 gaze 数据可解释。我们优先补鼠标、滚动、响应时间、AOI 和校准质量，同时记录光照、眼镜、坐姿、疲劳和设备上下文。远程实验可以在单独同意下保留 Zoom 录制作为辅助回看，但网页端不保存视频、人脸图像或截图，也不采集诊断身份。这样能把项目定位在任务中的学习状态与功能性支持需求，而不是身份分类。
