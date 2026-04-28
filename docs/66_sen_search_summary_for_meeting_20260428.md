# SEN Round 3 组会摘要

**日期**: 2026-04-28  
**输入**: `64_round3_sen_candidates_raw.csv`, `65_sen_delta_review_20260428.csv/md`  
**目的**: 把导师关于术语敏感性的反馈转化为可汇报的检索增量与下一步筛选任务。

## 1. 本轮做了什么

根据导师建议，本轮将检索重心从 `neurodivergent / neurodiversity` 扩展到学校语境中更常用的术语：

- `special educational needs`
- `special education needs`
- `SEN`
- `SEND`
- `students with special educational needs`
- `specific learning difficulties`
- `functional needs`
- `inclusive education`

同时保留 `neurodivergent / neurodiversity / ADHD / autism / dyslexia` 作为内部补充词，避免漏掉 HCI、LAK、EDM 中仍使用这些术语的前沿文献。

## 2. 自动检索结果

OpenAlex 自动检索共获得 130 条候选：

| Bucket | Raw | DOI/title 层面新增 |
| --- | ---: | ---: |
| SEN+Education | 35 | 35 |
| SEN+Adaptive | 35 | 34 |
| SEN+ObservableSignals | 35 | 35 |
| BridgeTerms | 25 | 20 |

与 `47_validated_master_v2_scored.csv` 对比后，124 条为 DOI/标题层面的新候选，6 条为重复 DOI。

## 3. 自动初筛结论

自动初筛是保守启发式，不是最终筛选。修正查询词虚高问题后：

| 自动建议 | 数量 | 含义 |
| --- | ---: | --- |
| screen_first | 1 | 标题层面同时命中 SEN/inclusion 与技术/适配，优先看摘要 |
| screen_second | 23 | 可能有用，但需人工确认是否真与 SEN + AI/自适应相关 |
| low_priority_or_noise | 100 | 多数是宽泛 AI、COVID、一般教育技术或跨域噪音 |
| duplicate_check | 6 | 旧 master 已覆盖或 DOI 重复 |

这说明 SEN 词表确实扩展了学校支持和 inclusive education 语境，但自动检索噪音明显高于原先 `neurodivergent` 定向检索，下一步需要摘要级人工筛选。

## 4. 第一批建议人工读摘要的候选

| Record ID | 建议原因 |
| --- | --- |
| R3SB016 | Inclusive higher education + specific learning difficulties + assistive technologies review，最贴近导师术语提醒和教育落地。 |
| R3SA001 / R3SE002 | Functional diversity + teachers' digital competence + logistic regression，能补“学校支持/教师能力/技术实施”视角。 |
| R3SE005 | UDL + technology systematic review，可补 inclusive design 与可及性设计框架。 |
| R3SE004 | Learning disabilities in higher education support，补 SEN 学生支持现状。 |
| R3SB021 | Neurodiversity + accessible university + ACM HCI，适合做 `neurodivergent` 与学校可及性术语的桥。 |
| R3SA006 | Students with SEND + higher education e-authentication，可补数字系统访问与可及性问题。 |
| R3SA018 | AI-driven multimodal personalized adaptive education for students with special needs，标题高度相关但引用少，需要查来源质量。 |
| R3SE025 | Computerized adaptive testing in students with and without disabilities，可作为 adaptive assessment 方向补充。 |

## 5. 对主线的影响

本轮初步支持一个更稳妥的对外口径：

> 我们根据导师建议，将对外用语从 neurodivergent-centered wording 调整为 SEN / SEND / functional learning needs。研究目标不是诊断某类学生，而是从学习行为、眼动和交互日志中推断学生在特定任务中的功能性支持需求。`neurodivergent` 仍作为补充检索词保留，因为 HCI 和 learning analytics 的前沿眼动文献仍大量使用该术语。

这个口径有两个好处：

1. **伦理更稳**：避免把 AI 系统说成识别或诊断学生身份。
2. **检索更广**：SEN/SEND 能覆盖学校支持、inclusive education、UDL、learning disabilities 等实践文献。

## 6. 下一步

1. 人工阅读上述 8 组候选的摘要，判断是否进入 keep_high / keep_medium。
2. 对 23 条 `screen_second` 做标题 + 摘要快速筛选。
3. 用 Google Scholar 手动抽查 `"special educational needs" "adaptive learning"`、`"SEN" "learning analytics" education`、`"SEND" "artificial intelligence" education` 前 30-50 条结果。
4. 若确认 5 篇以上高相关新增文献，再把它们并入后续 `Priority 40` 外的 “SEN addendum evidence set”。
