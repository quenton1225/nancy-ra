# 组会前剩余任务计划

**日期**: 2026-04-28  
**对应总计划**: `61_next_meeting_dual_deliverable_plan_20260428.md`  
**进度审计**: `71_next_meeting_progress_audit_20260428.md`  
**五样本眼动对比**: `73_eye_tracking_five_sample_comparison_20260428.md`  
**用途**: 作为明天继续推进的行动清单。

## 1. 当前总体状态

| 主线 | 当前完成度 | 状态判断 |
| --- | ---: | --- |
| SEN/SEND 术语替换与增量检索 | 约 70% | 自动检索、delta review、组会口径已完成；缺人工摘要筛选 |
| 普通笔记本眼动最小复现 | 约 92% | demo、P001-P005、特征提取、scanpath、五样本比较已完成 |
| 组会汇报材料整合 | 约 60% | 证据已经足够；需要整理成 slides 或 meeting brief |

当前最大的缺口不是眼动 demo，而是 SEN/SEND 新候选文献还没有完成摘要级人工筛选。眼动部分已经足够作为 feasibility proof 汇报，下一步重点是让它变成更清楚的一页结果，并规划下一版采集字段。

## 2. 明天优先任务

### 2.1 必做任务

| 顺序 | 任务 | 输入 | 输出 | 完成标准 |
| ---: | --- | --- | --- | --- |
| 1 | 人工筛选 SEN/SEND 优先候选 | `65_sen_delta_review_20260428.csv/md` | keep/maybe/exclude 清单 | 读完 `screen_first=1` 和 `screen_second=23` 的标题/摘要 |
| 2 | 形成 SEN addendum 初版 | 人工筛选结果 + `66_sen_search_summary_for_meeting_20260428.md` | 5-8 篇可向导师解释的新增证据 | 每篇有一句 relevance note |
| 3 | 整理 P001-P005 眼动结果一页版 | `73_eye_tracking_five_sample_comparison_20260428.md` | 组会可用结果页 | 包含 P005 baseline、P002 pressure test、P004 dim/backlit contrast |
| 4 | 准备 1 页 meeting brief | `61`, `66`, `71`, `73` | 可直接念/发的组会摘要 | 说明已完成、关键发现、下一步 |

### 2.2 尽量做任务

| 顺序 | 任务 | 目标 |
| ---: | --- | --- |
| 5 | 给 eye_tracking_demo 增加低负担上下文字段 | 记录光照、眼镜、头动/坐姿、疲劳、重复顺序 |
| 6 | 增加 response timing 和 calibration quality | 让下一轮 pilot 更容易判断数据质量 |
| 7 | Google Scholar 手动抽查 3 个 SEN 查询 | 补自动检索可能漏掉的文献 |

### 2.3 可以会后做

| 任务 | 延后理由 |
| --- | --- |
| A007/A008 ACM 全文补齐 | 需要机构访问；不影响当前 MVP 组会展示 |
| heatmap / fixation clustering / AOI dwell | 是可视化增强；scanpath 已能支撑 feasibility demo |
| baseline 分类/回归模型 | 当前样本量太小，不适合组会前强行建模 |
| 完整多模态字段全部实现 | 组会前可先讲 schema 和部分实现 |

## 3. SEN/SEND 文献主线明天怎么做

目标不是把所有 124 条新候选都读完，而是先把自动建议的优先候选变成可汇报的 evidence addendum。

### 3.1 输入文件

- `docs/65_sen_delta_review_20260428.csv`
- `docs/65_sen_delta_review_20260428.md`
- `docs/66_sen_search_summary_for_meeting_20260428.md`

### 3.2 操作步骤

1. 先筛 `screen_first=1` 的文献。
2. 再筛 `screen_second=23` 的文献。
3. 每篇只先做摘要级判断，不陷入全文精读。
4. 为每篇记录 decision: `keep`, `maybe`, `exclude`。
5. 为 keep/maybe 记录一句 relevance note。
6. 最后挑出 5-8 篇形成 `SEN addendum evidence set`。

### 3.3 判断标准

| decision | 标准 |
| --- | --- |
| keep | 明确涉及 SEN/SEND、higher education、learning support、digital/AI/learning analytics/assistive technology 中至少两项，并能服务本项目论证 |
| maybe | 相关但场景、年龄段、技术或研究对象有偏差，可能作为背景文献 |
| exclude | 只是在术语上相似，实际与高等教育学习支持或本项目无关 |

### 3.4 预期输出

建议新建一个后续文档：`75_sen_addendum_screening_20260429.md`。

它应包含：

1. 人工筛选摘要表；
2. keep/maybe/exclude 数量；
3. 5-8 篇优先新增文献；
4. 对导师可讲的 3 条发现；
5. 仍需全文确认的文献清单。

## 4. 眼动主线明天怎么做

眼动主线已经能证明 MVP 可行。明天重点不是继续无限收样本，而是把结果压缩成组会能看懂的一页，并规划下一轮采集更稳。

### 4.1 输入文件

- `docs/69_eye_tracking_mvp_pilot_log_20260428.md`
- `docs/70_eye_tracking_multimodal_data_collection_plan_20260428.md`
- `docs/73_eye_tracking_five_sample_comparison_20260428.md`
- `eye_tracking_demo/data/processed/features_P005_S1777388229181.csv`
- `eye_tracking_demo/data/visualizations/reading_gaze_P005_S1777388229181/index.html`

### 4.2 一页结果必须包含

1. P001-P005 样本条件表。
2. 五样本核心质量指标表。
3. 三个重点解释：
   - P005 是目前最干净的严格正常 baseline。
   - P002 说明眼镜和持续转头会明显降低 sampling density。
   - P004 说明略暗/逆光没有让 tracking 崩溃，但可能影响阅读行为。
4. 一张代表性 scanpath 图，优先选 P005 reading trial 或 P002/P005 对比。
5. 下一版采集字段列表。

### 4.3 下一版最小实现字段

如果明天有时间改 demo，优先加这些字段，不需要一次做完所有多模态计划。

| 字段组 | 具体字段 | 原因 |
| --- | --- | --- |
| participant context | participant_id, session_id, run_order | 支持重复实验和同一受试者对比 |
| condition context | lighting_condition, glasses, head_movement_instruction, posture_note | 解释 P002/P004/P005 这类条件差异 |
| timing | response_start_ms, response_submit_ms, response_latency_ms | 让 probe/quiz 行为可以量化 |
| calibration quality | calibration_click_count, calibration_elapsed_ms, simple_quality_note | 判断采集质量 |
| interaction context | mouse_x, mouse_y, scroll_y, active_aoi | 让 gaze 解释不再孤立 |

## 5. 组会汇报材料建议结构

建议做 5-8 页即可，不要太长。

| 页码 | 内容 | 主要证据 |
| ---: | --- | --- |
| 1 | 项目目标与术语调整 | 从 neurodivergent 对外调整为 SEN/SEND/functional learning needs |
| 2 | SEN/SEND 增量检索 | 130 条候选、124 条新候选、24 条优先筛选 |
| 3 | 眼动复现来源与边界 | WebGazer/C007；目标是 learning state/support needs，不是诊断 |
| 4 | MVP 流程 | calibration、reading、probe、quiz、CSV、scanpath |
| 5 | P001-P005 pilot 结果 | 五样本质量表 + P005/P002/P004 解释 |
| 6 | 当前结论 | 技术可行，但解释依赖上下文字段 |
| 7 | 下一步 | 人工筛文献、采集字段升级、小规模正式 pilot |

## 6. 明天结束时的理想交付物

| 交付物 | 文件建议 | 必要性 |
| --- | --- | --- |
| SEN 人工筛选结果 | `75_sen_addendum_screening_20260429.md` | 高 |
| 组会一页 brief | `76_next_meeting_brief_20260429.md` | 高 |
| 眼动一页结果 | 可并入 `76`，或单独 `77_eye_tracking_meeting_onepager_20260429.md` | 中高 |
| demo 字段升级 | `eye_tracking_demo/app.js`, `extract_features.py` | 中 |

## 7. 可直接使用的组会口径

> 目前我们已经完成两条主线的基础证据：第一，SEN/SEND 替代 neurodivergent 的增量检索已经得到 130 条候选，其中 24 条值得优先人工筛选；第二，普通笔记本 WebGazer MVP 已经通过 P001-P005 五个样本验证了采集、特征提取和 scanpath 可视化闭环。P005 是最干净的严格正常条件 baseline，P002 显示眼镜和持续转头会明显降低采样密度，P004 显示略暗逆光没有直接破坏 tracking。下一步不是马上训练模型，而是完成 SEN 摘要筛选，并把光照、眼镜、头动、响应时间、AOI 和校准质量写入下一版数据 schema。

## 8. 明天开始的第一步

从 SEN/SEND 人工筛选开始。原因是眼动主线已经有可展示结果，而文献主线目前还缺人工判断；先补这个缺口，组会材料会更平衡。
