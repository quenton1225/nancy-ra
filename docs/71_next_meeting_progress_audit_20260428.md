# 下次组会任务完成度审计

**日期**: 2026-04-28  
**对应总计划**: `61_next_meeting_dual_deliverable_plan_20260428.md`  
**结论**: 组会前已经具备可汇报的两条主线材料；眼动 pilot 已扩展到 5 个样本和 2 组受试条件，SEN/SEND 优先候选已完成摘要筛选、A1-A7/B1 全文提取和组会证据表，中文 meeting brief 与下一版采集 schema 已完成；还差正式 slides 或把采集字段实现到 demo。

## 1. 总体判断

| 主线 | 当前完成度 | 组会可讲程度 | 还差什么 |
| --- | ---: | --- | --- |
| SEN/SEND 术语替换与增量检索 | 约 88% | 可以汇报检索策略、OpenAlex 增量、摘要筛选、A1-A7/B1 全文判断和组会证据表 | Google Scholar 手动补充、最终 brief/slides 整合 |
| 普通笔记本眼动最小复现 | 约 94% | 可以现场展示 demo、P001-P005 五样本分析、scanpath 图和下一版数据 schema | 把多模态行为字段实现到 demo，形成更稳的质量门槛 |
| 组会汇报材料整合 | 约 90% | 中文 `78_next_meeting_brief_20260429.md` 已完成，可拆成 5-8 页 slides | 还差正式 slides 或口头讲稿微调 |

## 2. GO-61-A: SEN/SEND 增量检索状态

### 2.1 已完成

| 项目 | 证据文件 | 状态 |
| --- | --- | --- |
| SEN 查询协议 | `62_sen_search_protocol_20260428.md` | 完成 |
| OpenAlex 自动采集脚本 | `scripts/collect_round3_sen_openalex.py` | 完成并已运行 |
| 原始候选表 | `64_round3_sen_candidates_raw.csv` | 完成，130 条 |
| 采集日志 | `64_round3_sen_collection_log.md` | 完成 |
| 新旧文献池 delta review | `65_sen_delta_review_20260428.md/csv` | 完成，124 条 DOI/title 新候选 |
| 组会口径摘要 | `66_sen_search_summary_for_meeting_20260428.md` | 完成 |
| 摘要级筛选与下载清单 | `75_sen_addendum_abstract_screening_20260429.md` | 完成，21 篇优先候选去重判断 |
| A1-A7/B1 全文证据提取 | `76_sen_fulltext_evidence_extraction_20260429.md` | 完成 |
| 组会文献证据表 | `77_next_meeting_literature_evidence_table_20260429.md` | 完成，可直接放入 brief/slides |

### 2.2 当前结果

- OpenAlex 共采集 130 条候选。
- DOI/title 层面新增 124 条，重复 DOI 6 条。
- 自动建议 `screen_first=1`, `screen_second=23`, `low_priority_or_noise=100`。
- 术语口径已从 `neurodivergent` 对外中心，调整为 `SEN / SEND / functional learning needs` 对外中心；`neurodivergent` 保留为内部补充检索词。

### 2.3 剩余任务

| 优先级 | 任务 | 目标输出 | 是否必须在组会前完成 |
| --- | --- | --- | --- |
| 已完成 | 人工读 1 条 `screen_first` + 23 条 `screen_second` 摘要 | `75_sen_addendum_abstract_screening_20260429.md` | 已完成 |
| 已完成 | 对 A1-A7/B1 做全文级 evidence extraction | `76_sen_fulltext_evidence_extraction_20260429.md`, `77_next_meeting_literature_evidence_table_20260429.md` | 已完成 |
| 中 | Google Scholar 手动抽查 3 个 SEN 查询 | 手动补充候选表 | 可部分完成 |
| 中 | ACM / 机构访问补全文 | 新增全文或截图式访问记录 | 可延后 |
| 低 | 将确认 keep 的新增文献并入后续 evidence set | `SEN addendum evidence set` | 可会后完成 |

## 3. GO-61-B: 眼动最小复现状态

### 3.1 已完成

| 项目 | 证据文件/目录 | 状态 |
| --- | --- | --- |
| 复现 playbook | `63_webcam_eye_tracking_replication_playbook_20260428.md` | 完成 |
| 核心论文 source pack | `67_eye_tracking_source_pack_20260428.md` | 完成，C007 可直接支撑 MVP |
| demo 设计 | `68_eye_tracking_demo_design_20260428.md` | 完成 |
| WebGazer MVP | `eye_tracking_demo/` | 完成，本地可运行 |
| WebGazer/MediaPipe 资源修复 | `eye_tracking_demo/vendor/`, `eye_tracking_demo/mediapipe/` | 完成，避免 CDN/404 问题 |
| 特征提取脚本 | `eye_tracking_demo/analysis/extract_features.py` | 完成，P001-P005 已运行 |
| scanpath 可视化脚本 | `eye_tracking_demo/analysis/render_scanpaths.py` | 完成，P001-P005 已运行 |
| P001 pilot | `69_eye_tracking_mvp_pilot_log_20260428.md` | 完成，质量较好 |
| P002 pressure pilot | `69_eye_tracking_mvp_pilot_log_20260428.md` | 完成，眼镜 + 转头条件下仍可用但采样率下降 |
| P003/P004 condition pilots | `72_eye_tracking_four_sample_comparison_20260428.md` | 完成，受试者 2 正常光照与略暗逆光对比 |
| P005 strict baseline pilot | `73_eye_tracking_five_sample_comparison_20260428.md` | 完成，受试者 1 不戴眼镜、正常光、严格避免转头基线 |
| 多模态采集规划 | `70_eye_tracking_multimodal_data_collection_plan_20260428.md` | 完成，尚未实现 |
| 下一版采集 schema | `79_next_eye_tracking_data_collection_schema_20260429.md` | 完成，包含 pointer/scroll/latency/AOI/calibration/Zoom 辅助记录 |

### 3.2 当前结果

| 指标 | P001 | P002 | P003 | P004 | P005 | 判断 |
| --- | ---: | ---: | ---: | ---: | ---: | --- |
| gaze rows | 8494 | 3419 | 12915 | 6225 | 5614 | P003 数据量最大，P002 最少 |
| average gaze Hz | 50.0 | 27.4 | 49.6 | 50.0 | 47.6 | P002 采样密度明显下降，其余接近 48-50Hz |
| overall offscreen ratio | 0.0274 | 0.0140 | 0.0132 | 0.0050 | 0.0082 | 五者都可接受 |
| reading trials | 3 | 3 | 3 | 3 | 3 | 全部完整 |
| TUT positive trials | 1 | 1 | 3 | 3 | 0 | P005 最干净，受试者 2 两轮均全为 TUT=1 |
| quiz correct | 3/3 | 2/3 | 2/3 | 2/3 | 3/3 | P001/P005 理解题全对 |
| scanpath SVGs | 8 | 8 | 8 | 8 | 8 | 均已生成 |

### 3.3 剩余任务

| 优先级 | 任务 | 目标输出 | 是否必须在组会前完成 |
| --- | --- | --- | --- |
| 高 | 把眼镜、光线、坐姿、转头等上下文字段加入采集 | 更新版 CSV schema | 建议完成至少部分 |
| 高 | 加 mouse/pointer、scroll、response timing、AOI、calibration quality | `app.js` + `extract_features.py` 更新 | 如果要展示“下一版更稳”，建议完成 |
| 中 | 对 scanpath 加 fixation/heatmap/AOI dwell 汇总 | 更接近眼动研究常用输出 | 可部分完成 |
| 中 | 再收 1-2 个正常光照样本 | 检查五样本趋势是否稳定 | 可选 |
| 中 | 下载 A007/A008 ACM 全文 | source pack 更新 | 需要机构访问，可延后 |
| 低 | 做 baseline 分类/回归模型 | feasibility report | 当前样本量不足，不建议组会前强做 |

## 4. 组会前建议优先级

### 必做

1. 把 P001-P005 的 feature table 和 scanpath 图整理成一页结果。
2. 把 `77_next_meeting_literature_evidence_table_20260429.md` 和五样本眼动结果整合成最终 meeting brief/slides。
3. 明确下一版必须记录光照、眼镜、转头/坐姿、重复顺序和校准质量。
4. 准备清楚口径: 本项目不是诊断学生，而是推断任务中的学习状态和支持需求。

### 尽量做

1. 在 demo 中加入眼镜、光线、坐姿/转头、疲劳等低负担上下文字段。
2. 加入 response timing 和 calibration quality；这两个对解释质量最有价值。
3. 对 Google Scholar 做一轮手动抽查，补自动检索可能漏掉的 SEN 文献。

### 可以会后做

1. 热图、fixation clustering、AOI dwell 的完整可视化。
2. A007/A008 全文补齐和精读。
3. 模型训练或 formal evaluation。

## 5. 当前可直接汇报的一句话

> 组会前的两件事已经从计划推进到可展示证据：SEN/SEND 术语增量检索已得到 130 条候选，并完成了优先候选摘要筛选、A1-A7/B1 全文提取、组会文献证据表和中文 meeting brief；普通笔记本 WebGazer MVP 已完成，并通过 P001-P005 五个样本验证了采集、特征提取和 scanpath 可视化闭环。P005 是目前最严格的正常条件基线，P002 显示眼镜和持续转头会降低采样密度，P004 显示略暗逆光没有导致追踪崩溃但可能改变阅读行为。下一版采集 schema 已明确优先补鼠标、滚动、响应时间、AOI、校准质量，以及 Zoom 远程实验的独立辅助记录。下一步重点不是马上建模型，而是把 brief 拆成 slides 或把采集 schema 实现到 demo。
