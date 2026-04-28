# 下次组会双交付执行计划

**日期**: 2026-04-28  
**目标受众**: DU / Nancy / 导师组会准备  
**阶段性质**: 术语校准 + 文献增量检索 + 眼动技术可行性复现

## 0. 是否借鉴 llm-memory-management 的组织方式

结论: **需要借鉴，但只借鉴轻量结构，不照搬完整实验仓库体系。**

`llm-memory-management` 的优点是清楚地区分了三层内容:

1. 主线层: 当前有效状态、阶段目标、历史/弃用边界、更新规则。
2. 执行层: 每个阶段有 playbook，写明输入、输出、门槛、风险、回滚点。
3. 结果层: 原始结果不塞进主线文档，只保存在结果文件或阶段 summary 中。

本项目已经有稳定的 `docs/编号_标题_日期` 风格，因此采用如下轻量版:

| 层级 | 本项目采用方式 | 本轮文件 |
| --- | --- | --- |
| 主线计划 | 用 1 个编号文档回答“现在做什么、为什么做、怎么验收” | `61_next_meeting_dual_deliverable_plan_20260428.md` |
| 执行 playbook | 每个交付物 1 个执行入口 | `62_sen_search_protocol_20260428.md`; `63_webcam_eye_tracking_replication_playbook_20260428.md` |
| 结果记录 | 新检索/复现结果用独立 csv/md 记录，避免污染旧文献池 | 预计 `64_*`, `65_*`, `66_*`, `67_*` |

不建议现在新建复杂的 `experiments/` 体系，因为本项目当前核心资产是文献证据、全文锚点和小型技术原型；过早重构目录会增加维护成本。

## 1. 当前状态判断

已有基础:

- 166 条 scored master 记录: `docs/47_validated_master_v2_scored.csv`。
- 40 篇 balanced priority 文献: `docs/53_fulltext_priority40_balanced.csv`。
- 40/40 摘要覆盖与 12 篇重点文献锚点: `docs/54_crossref_abstracts_40.csv`, `docs/55_key_papers_deep_dive_20260410.md`, `docs/58_fulltext_anchor_progress_20260411.md`。
- 研究主线已从“诊断标签”转向“functional needs inference”: `docs/01_unified_project_brief.md` 与 `Notes from Nancy_20260317.txt`。

关键缺口:

- 当前查询与组名仍以 `neurodivergent / neurodiversity` 为中心，学校语境中的 `special educational needs / SEN / SEND` 覆盖不足。
- 眼动方向已有 3 篇高度相关论文条目，但本地全文与补充材料尚未收齐，不能直接声称完整复现。
- 眼动复现若以“识别 neurodivergent/SEN 学生”为目标，伦理与性能风险较高；更稳妥的目标是先复现“普通笔记本摄像头能否捕捉学习状态信号”。

## 2. 本轮两个交付物

### GO-61-A: SEN 词表增量检索包

目标: 回应导师关于术语敏感性的提醒，用学校实践中更常见的 `special educational needs / SEN / SEND` 词表重跑一轮增量检索，判断是否发现旧词表遗漏的重要文献。

最终输出:

- `docs/62_sen_search_protocol_20260428.md`: SEN 查询词表、筛选规则、验收门槛。
- `scripts/collect_round3_sen_openalex.py`: OpenAlex 自动采集脚本。
- `docs/64_round3_sen_candidates_raw.csv`: 自动采集原始候选。
- `docs/64_round3_sen_collection_log.md`: 采集日志。
- `docs/65_sen_delta_review_20260428.md`: 与旧 master 文献池对比后的新增发现与汇报口径。

验收条件:

- 至少完成 OpenAlex 自动检索；若网络或 API 阻塞，保留失败日志和手动检索清单。
- 候选表至少按 `SEN+Education`, `SEN+Adaptive`, `SEN+AI/Analytics` 三类分桶。
- 与旧 master 通过 DOI/标题做 delta 对比，避免把旧文献当作新发现。
- 输出一段可直接汇报给导师的术语修正口径。

### GO-61-B: 普通笔记本眼动最小复现包

目标: 基于 WebGazer / webcam-based eye tracking 论文，先做“可行性复现”，验证普通笔记本摄像头能否采集阅读任务中的 gaze 数据并生成可分析特征。

最终输出:

- `docs/63_webcam_eye_tracking_replication_playbook_20260428.md`: 复现路线、技术栈、输入输出、伦理边界。
- `docs/67_eye_tracking_source_pack_20260428.md`: A007/C007/A008 全文、数据、代码、补充材料追踪表。
- 预计后续 `eye_tracking_demo/`: WebGazer 采集 demo 与说明。
- `docs/69_eye_tracking_mvp_pilot_log_20260428.md`: 小样本 pilot 日志与可行性结论。

验收条件:

- 明确不把 MVP 目标写成“诊断学生身份”；只做 TUT、阅读困难、文本熟悉度、理解表现等学习状态代理指标。
- 先收齐/追踪 3 篇核心眼动论文的全文与补充材料状态。
- demo 不保存原始视频，只保存 gaze 坐标、时间戳、任务事件、probe 回答和理解题结果。
- 若无法立即完成完整 demo，也要形成可执行技术路线和依赖清单。

## 3. GO-61-A 工作流: SEN 增量检索

| 步骤 | 任务 | 输入条件 | 输出 | 出口条件 | 是否需要用户协助 |
| --- | --- | --- | --- | --- | --- |
| A0 | 术语锁定 | 导师反馈、现有 project brief | 对外/对内术语表 | 明确 `SEN` 对外优先，`neurodivergent` 作为补充检索词 | 不需要 |
| A1 | 查询包设计 | `docs/02_scholar_search_protocol.md`, 旧脚本查询 | `docs/62_sen_search_protocol_20260428.md` | 查询覆盖 SEN/SEND/inclusive education/learning difficulties | 不需要 |
| A2 | OpenAlex 自动采集 | A1 完成，网络可用 | `64_round3_sen_candidates_raw.csv`, log | 每个分桶尽量达到 25-40 条候选 | 不需要，除非 API 失败 |
| A3 | Google Scholar/ACM 手动补充 | A1 查询包 | 手动候选补充表 | 每条核心查询前 30-50 条结果至少抽查 | 需要；Scholar 容易触发验证码，ACM 可能要机构访问 |
| A4 | 去重与 delta 对比 | 新 raw + `47_validated_master_v2_scored.csv` | `65_sen_delta_review_20260428.md` | DOI/标题去重，列出新增和旧池已有 | 不需要 |
| A5 | 快速筛选 | A4 delta 表 | keep/maybe/exclude 初筛 | 保留 10-20 篇值得深读的新增文献 | 可能需要你确认范围边界 |
| A6 | 组会口径 | A5 结果 | 汇报段落 | 能解释“为什么术语调整后研究更稳” | 不需要 |

## 4. GO-61-B 工作流: 眼动最小复现

| 步骤 | 任务 | 输入条件 | 输出 | 出口条件 | 是否需要用户协助 |
| --- | --- | --- | --- | --- | --- |
| B0 | 核心论文源追踪 | A007/C007/A008 条目 | `67_eye_tracking_source_pack_20260428.md` | 标记全文、数据、代码、补充材料是否可得 | 需要；ACM/EDM 全文可能要你下载或提供访问 |
| B1 | 复现目标收窄 | B0 至少有摘要级方法 | `63` 中的目标定义 | 目标改为学习状态信号，不做诊断分类承诺 | 不需要 |
| B2 | MVP 技术方案 | WebGazer + 浏览器 + CSV 导出 | demo 设计稿 | 明确采集字段、任务流程、隐私边界 | 不需要 |
| B3 | 采集 demo 实现 | B2 完成 | `eye_tracking_demo/` | 本机浏览器可运行，能导出 gaze/event/probe 数据 | 需要你允许浏览器摄像头权限做试跑 |
| B4 | 特征提取 | B3 产生样例数据 | feature table | 生成离屏比例、gaze dispersion、阅读时长等特征 | 需要至少 1-3 个 pilot 样本更好 |
| B5 | baseline 分析 | B4 特征表 + probe 标签 | 简单 notebook/report | 输出可行性结论，不夸大模型效果 | 可能需要你判断任务材料是否适合 |
| B6 | 伦理与组会口径 | B3-B5 | 风险说明 | 明确不存视频、不做诊断、先做技术可行性 | 不需要 |

## 5. 用户协助清单

优先级最高的协助:

1. **下载全文**: A007, C007, A008 的 ACM/EDM PDF、supplementary materials、可能的 dataset/code link。
2. **Google Scholar 手动抽查**: 按 `62` 中查询式查看前 30-50 条，避免 OpenAlex 漏掉灰色文献或高相关会议论文。
3. **浏览器摄像头试跑**: 眼动 demo 完成后，需要你在本机允许摄像头权限，试跑一次校准和阅读任务。

可选协助:

- 帮忙确认学校/导师组更偏好的术语: `SEN`, `SEND`, `students with disabilities`, `additional learning support needs`。
- 帮忙确认实验材料语言: 英文阅读文本、中文阅读文本，或与未来学习任务一致的课程材料。

## 6. 风险与预案

| 风险 | 影响 | 预案 |
| --- | --- | --- |
| `SEN` 缩写噪音大 | 检索结果混入无关领域 | 查询中强制搭配 `education`, `learning`, `students`, `adaptive learning` |
| Google Scholar 自动化困难 | 无法完全自动复现 Scholar 检索 | OpenAlex 先跑，Scholar 由用户手动抽查并记录 |
| 眼动论文全文不可得 | 无法严格复现原文参数 | 先做“方法启发式复现”，明确标注非严格 reproduction |
| WebGazer 精度受光线/摄像头影响 | pilot 数据噪声大 | 把结论限定为采集可行性，先不承诺高准确率 |
| 诊断分类伦理敏感 | 组会被质疑 | 统一改成 functional needs / learning state inference |

## 7. 推荐执行顺序

本轮按以下顺序推进:

1. 完成 `62` 和 `63` 两个执行入口。
2. 先跑 SEN OpenAlex 自动检索，得到 raw candidates。
3. 做新旧文献池 delta 对比，产出新增发现清单。
4. 同步追踪眼动 3 篇核心论文全文/补充材料。
5. 若全文或方法足够，启动 WebGazer MVP；否则先完成 source pack 和复现边界说明。

## 8. 当前 GO / NO-GO 判据

- GO-61-A 现在可以启动: 旧脚本和 master 表齐全。
- GO-61-B 可以启动 source tracking 和 playbook；完整 demo 依赖全文/补充材料与本机摄像头试跑。
