# SEN 词表增量检索执行协议

**日期**: 2026-04-28  
**对应总计划**: `61_next_meeting_dual_deliverable_plan_20260428.md`  
**目的**: 用学校与政策语境更常见的 `special educational needs / SEN / SEND` 词表补跑一轮文献检索，形成对导师反馈的可追溯回应。

## 1. 术语策略

对外汇报优先使用:

- special educational needs (SEN)
- special educational needs and disabilities (SEND)
- students with special educational needs
- inclusive education
- additional learning support needs
- functional needs / learning support needs

内部补充检索保留:

- neurodivergent / neurodiversity
- autism / ADHD / dyslexia / learning disabilities

原因: `SEN/SEND` 更贴近学校实践与政策口径；`neurodivergent` 在 HCI、LAK、EDM 新文献中仍然是重要前沿词，不应完全删除。

## 2. 查询分桶

### Bucket A: SEN + Education

目标: 找学校支持、包容教育、课堂策略和学习结果文献。

OpenAlex/Scholar 查询:

1. `"special educational needs" students learning support higher education`
2. `"special education needs" inclusive education learning outcomes`
3. `SEN students education technology learning support`
4. `SEND students inclusive education higher education`
5. `"students with special educational needs" learning difficulties education`

### Bucket B: SEN + Adaptive Learning / Educational Technology

目标: 找 AI、自适应学习、个性化系统、学习分析与 SEN 的交叉证据。

OpenAlex/Scholar 查询:

1. `"special educational needs" adaptive learning system`
2. `"special educational needs" artificial intelligence education`
3. `SEN adaptive learning educational technology`
4. `SEND learning analytics adaptive support students`
5. `"learning difficulties" personalized learning system AI`

### Bucket C: SEN + Observable Signals / Learning Analytics

目标: 找从行为、眼动、日志或学习表现推断支持需求的证据。

OpenAlex/Scholar 查询:

1. `"special educational needs" learning analytics prediction`
2. `SEN students eye tracking learning`
3. `"students with special educational needs" machine learning education`
4. `"learning disabilities" eye tracking reading comprehension machine learning`
5. `"inclusive education" learning analytics intervention`

### Bucket D: Bridge Terms

目标: 找 `SEN` 与 `neurodiversity` 之间的桥接文献，帮助组会解释术语切换不等于研究方向改变。

OpenAlex/Scholar 查询:

1. `neurodiversity "special educational needs" education`
2. `neurodivergent students "special educational needs"`
3. `autism ADHD dyslexia "special educational needs" adaptive learning`
4. `"functional needs" students adaptive learning eye tracking`

## 3. 自动检索规则

数据源:

- OpenAlex API: 自动脚本先跑，保证可重复。
- Google Scholar: 手动抽查补充，记录查询日期和前 30-50 条中新增候选。
- ACM/IEEE/EDM/LAK: 针对眼动和学习分析主题手动补充。

过滤条件:

- 年份优先: 2020+。
- 必须包含教育、学习、学生、课堂、包容教育或学习技术语境之一。
- `SEN` 缩写必须和 `education/learning/student` 同时出现，否则不纳入。
- 优先保留 empirical study、systematic review、rapid review、learning analytics / AI / adaptive system 论文。

排除条件:

- 纯医疗诊断且与学习支持无关。
- 政策评论但没有可转移变量或支持策略。
- 只出现 `SEN` 但语义不是 special educational needs。
- 无标题、年份、来源或摘要的记录。

## 4. 输出字段

自动采集表沿用 master schema 的核心字段:

- `record_id`
- `title`
- `authors`
- `year`
- `venue`
- `publication_type`
- `doi`
- `source_url`
- `citation_count`
- `bucket`
- `query_string`
- `domain_sen`
- `domain_education`
- `domain_adaptive`
- `input_signal`
- `ai_method`
- `prediction_target`
- `decision`
- `notes`

## 5. 入出条件

### A1 查询包设计

输入:

- 导师反馈。
- 旧检索协议 `docs/02_scholar_search_protocol.md`。
- 当前 master 与 priority 文献池。

输出:

- 本文件。

出口条件:

- 至少 3 个主分桶 + 1 个 bridge 分桶。
- 每个分桶至少 4 条可直接复制的查询式。

### A2 OpenAlex 自动采集

输入:

- 本文件查询式。
- `scripts/collect_round3_sen_openalex.py`。

输出:

- `docs/64_round3_sen_candidates_raw.csv`。
- `docs/64_round3_sen_collection_log.md`。

出口条件:

- 自动脚本成功运行并记录每个分桶条数；若失败，记录错误与替代手动方案。

### A3 手动补充

输入:

- 本文件查询式。
- Google Scholar / ACM / EDM 页面。

输出:

- 手动候选记录，可追加到后续 delta review。

出口条件:

- 每条最重要查询至少看前 30-50 条，标记新增/已见/无关。

用户协助:

- Google Scholar 可能触发验证码，建议由用户手动查看。
- ACM/EDM 可能需要机构网络或账号下载全文。

### A4 Delta Review

输入:

- 新候选表。
- `docs/47_validated_master_v2_scored.csv`。

输出:

- `docs/65_sen_delta_review_20260428.md`。

出口条件:

- DOI/title 去重完成。
- 列出新增高潜力候选、旧池已覆盖候选和需要人工确认候选。

## 6. 组会汇报口径

建议表述:

> 根据导师提醒，我们把对外术语从 neurodivergent-centered wording 调整为 school-facing SEN/SEND and functional learning needs wording。新的检索不会删除原有 neurodiversity 文献，而是把它作为补充入口，用 SEN/SEND 词表检查学校实践语境中是否有遗漏证据。这样既降低术语敏感性，也能扩大教育政策和学校支持领域的覆盖。
