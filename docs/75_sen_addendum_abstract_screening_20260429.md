# SEN/SEND Addendum Abstract Screening and Full-Text Request List

**日期**: 2026-04-29  
**来源**: `65_sen_delta_review_20260428.csv/md`  
**对应计划**: `74_next_meeting_remaining_work_plan_20260428.md`  
**目的**: 对 `screen_first` 和 `screen_second` 候选做摘要级筛选，判断哪些文章值得优先下载正文。

**后续全文筛选**: 用户已下载 A1-A7/B1，全文级 evidence extraction 见 `76_sen_fulltext_evidence_extraction_20260429.md`。

## 1. Scope and Method

本轮只筛自动建议的优先候选：

- priority rows: 24
- unique works after DOI/title deduplication: 21
- 摘要来源: DOI/title 查询 OpenAlex abstract；部分出版社页面抽查。

去重说明：

- `Ethical principles for artificial intelligence in education` 同时出现在 R3SA032/R3SE032/R3SO005，按 1 篇处理。
- `Teachers' digital competence to assist students with functional diversity` 同时出现在 R3SA001/R3SE002，按 1 篇处理。

出版社页面访问情况：

- Springer/OpenAlex 摘要可用。
- ACM、IEEE、Wiley、Sage 页面自动抓取受到 403/418 限制；这些文章如果被列为 priority，需要用户通过学校或机构渠道下载正文。

## 2. Full-Text Download Priority

### 2.1 Priority A: Please download full text first

这些文章最值得优先下载正文。它们和本项目的核心关系最强：SEN/SEND、高等教育、技术支持、学习状态/适应性系统、可观测数据。

| Priority | Record ID | Title | DOI | Why full text is needed |
| --- | --- | --- | --- | --- |
| A1 | R3SB016 | From Assistive Technologies to Metaverse—Technologies in Inclusive Higher Education for Students With Specific Learning Difficulties: A Review | 10.1109/access.2023.3289496 | 最直接命中“higher education + learning difficulties + assistive technologies”。需要正文提取技术类别、挑战、future directions，可作为 SEN 技术支持主证据。 |
| A2 | R3SE004 | Educational Support for Saudi Students with Learning Disabilities in Higher Education | 10.1111/ldrp.12214 | 明确是高等教育中 learning disabilities 学生的 support requirements。需要正文看访谈主题、支持服务缺口和可迁移性。 |
| A3 | R3SB021 | Neurodiversity and the Accessible University: Exploring Organizational Barriers, Access Labor and Opportunities for Change | 10.1145/3641011 | 虽然标题用 neurodiversity，但内容是大学环境、access barriers、assistive technology access、cognitive/social access。需要正文支撑“大学组织层面的支持需求”。 |
| A4 | R3SA006 | Acceptability of the e-authentication in higher education studies: views of students with special educational needs and disabilities | 10.1186/s41239-020-00236-9 | 明确 SEND + higher education + 技术系统接受度，样本为 267 名 SEND 学生。需要正文看学生对技术失败、误判、信任的担忧。 |
| A5 | R3SA018 | AI-Driven Innovation Using Multimodal and Personalized Adaptive Education for Students With Special Needs | 10.1109/access.2025.3560863 | 与我们下一步“多模态 + adaptive support + special needs”高度贴近。需要正文核查数据来源、模型方法、XAI、是否真实实验。 |
| A6 | R3SA031 | Artificial Intelligence and Sensor Technologies the Future of Education Students with and without Intellectual and Developmental Disabilities | 10.56769/ijpn09102 | 摘要直接提到 wearable sensors、physiological signals、learning status、cognitive states、real-time adaptation。需要正文判断质量和是否可作为眼动/传感器路线依据。 |
| A7 | R3SO028 | Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance | 10.1111/bjet.13544 | 不专注 SEN，但和“学习过程、AI 支持、multi-channel learning/process data、自我调节”高度相关。需要正文借鉴实验设计、过程数据和学习状态解释方式。 |

如果时间只能下载 5 篇，优先下载 A1-A5。A6 很贴近眼动/传感器路线，但要警惕期刊和方法质量；A7 更偏学习过程方法论，不是 SEN 主证据。

### 2.2 Priority B: Download if time allows

这些文章有用，但不一定是组会前最关键的全文。

| Priority | Record ID | Title | DOI | Abstract-level judgment |
| --- | --- | --- | --- | --- |
| B1 | R3SA022 | The Use of Adaptive Learning Technologies in e-Learning for Inclusive Education: A Systematic Review | 10.57125/elij.2024.03.25.05 | 命中 inclusive education + adaptive/e-learning + SEN，但 venue 可信度需要核查。正文可帮助判断是否能作为系统综述证据。 |
| B2 | R3SE005 | What next for Universal Design for Learning? A systematic literature review of technology in UDL implementations at second level | 10.1111/bjet.13328 | UDL + technology 很有理论价值，但场景是 second level，不是 higher education。可作为 design framework，不是核心 evidence。 |
| B3 | R3SA001/R3SE002 | Teachers' digital competence to assist students with functional diversity: Identification of factors through logistic regression methods | 10.1111/bjet.13151 | functional diversity + digital resources + teacher competence；但重点是教师能力，不是学生学习状态。正文可作为机构/教师准备度背景。 |
| B4 | R3SO027 | Artificial intelligence applications in Latin American higher education: a systematic review | 10.1186/s41239-022-00326-w | AI in higher education 背景综述，摘要提到 assistive technology、predictive modelling、learning analytics。正文可用于 AI in HE 背景，不是 SEN 主证据。 |
| B5 | R3SO015 | AI-Based Personalized E-Learning Systems: Issues, Challenges, and Solutions | 10.1109/access.2022.3193938 | 个性化 e-learning 综述，能支持 adaptive learning 论述，但摘要没有 SEN/SEND 或高等教育特异性。 |

## 3. Abstract-Level Screening Table

| Record ID | Title | Abstract-level decision | Need full text? | Reason |
| --- | --- | --- | --- | --- |
| R3SB016 | From Assistive Technologies to Metaverse—Technologies in Inclusive Higher Education for Students With Specific Learning Difficulties: A Review | keep | Yes, Priority A | 直接覆盖 inclusive higher education、students with learning difficulties、assistive technologies。 |
| R3SE004 | Educational Support for Saudi Students with Learning Disabilities in Higher Education | keep | Yes, Priority A | 高等教育 LD 学生支持需求，和项目问题定义高度贴近。 |
| R3SB021 | Neurodiversity and the Accessible University: Exploring Organizational Barriers, Access Labor and Opportunities for Change | keep | Yes, Priority A | 大学场景、组织障碍、access labor、assistive/cognitive/social access，适合补充“支持需求”理论。 |
| R3SA006 | Acceptability of the e-authentication in higher education studies: views of students with special educational needs and disabilities | keep | Yes, Priority A | SEND 学生对技术系统的接受度和风险感知，能提醒我们不要只谈技术有效性。 |
| R3SA018 | AI-Driven Innovation Using Multimodal and Personalized Adaptive Education for Students With Special Needs | keep | Yes, Priority A | 多模态、个性化、自适应、special needs，和下一版 eye-tracking/multimodal plan 直接相关。 |
| R3SA031 | Artificial Intelligence and Sensor Technologies the Future of Education Students with and without Intellectual and Developmental Disabilities | keep/maybe | Yes, Priority A | 摘要非常贴近 sensor/cognitive state/real-time adaptation，但需要全文核查质量和实证程度。 |
| R3SO028 | Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance | keep/method | Yes, Priority A | 不是 SEN 文献，但有大学生、AI 支持、学习过程、多通道数据和 SRL 序列，可借鉴方法。 |
| R3SA022 | The Use of Adaptive Learning Technologies in e-Learning for Inclusive Education: A Systematic Review | maybe/keep | Optional, Priority B | inclusive + adaptive + SEN；但需要正文核查综述质量和数据库范围。 |
| R3SE005 | What next for Universal Design for Learning? A systematic literature review of technology in UDL implementations at second level | maybe | Optional, Priority B | UDL 技术框架有用，但教育阶段不是 higher education。 |
| R3SA001/R3SE002 | Teachers' digital competence to assist students with functional diversity | maybe | Optional, Priority B | 支持教师/机构能力背景，但不直接回答学生学习状态检测。 |
| R3SO027 | Artificial intelligence applications in Latin American higher education: a systematic review | maybe/background | Optional, Priority B | AI in HE 背景有用，摘要提到 assistive technology/predictive modelling；SEN 特异性弱。 |
| R3SO015 | AI-Based Personalized E-Learning Systems: Issues, Challenges, and Solutions | maybe/background | Optional, Priority B | 可支持个性化学习系统背景，SEN/HE 特异性弱。 |
| R3SA032/R3SE032/R3SO005 | Ethical principles for artificial intelligence in education | background | Not now | AI ethics 重要，但摘要没有 SEN/SEND 或高等教育支持需求特异性。可用摘要层面判断，组会前不必下载。 |
| R3SO008 | Embracing the future of Artificial Intelligence in the classroom | background | Not now | AI literacy/prompt engineering/critical thinking 综述，提到 special needs 但不是主线。 |
| R3SO030 | Empowering learners for the age of artificial intelligence | background | Not now | 特刊导论/主题综述性质，适合宽背景，不需要优先全文。 |
| R3SO007 | Artificial Intelligence in Education: AIEd for Personalised Learning Pathways | background | Not now | 个性化学习路径概念背景，SEN/SEND 和 HE 关联不足。 |
| R3SO019 | AI-driven adaptive learning for sustainable educational transformation | background/no | Not now | 偏 bibliometric/sustainable transformation，和 SEN 支持或学习状态检测距离较远。 |
| R3SO020 | A critical evaluation, challenges, and future perspectives of using artificial intelligence and emerging technologies in smart classrooms | background/no | Not now | smart classroom/AI survey，宽泛背景，SEN/SEND 不突出。 |
| R3SO017 | Human-in-the-loop machine learning: a state of the art | method background | Not now | 可作为 HITL 方法背景，但不是教育/SEN 文献。 |
| R3SO024 | A Machine Learning and Multi-Criteria Decision-Making Framework for Student Grade Prediction | exclude/maybe | No | 学生成绩预测和可解释 ML，几乎没有 SEN/HE support needs 直接关系。 |
| R3SO022 | Human- versus Artificial Intelligence | exclude | No | 摘要信息很弱，和本项目关系过泛，不建议组会前投入。 |

## 4. Recommended Download List for User

请优先尝试下载以下全文。

### Must download

| Record ID | Title | DOI | Access note |
| --- | --- | --- | --- |
| R3SB016 | From Assistive Technologies to Metaverse—Technologies in Inclusive Higher Education for Students With Specific Learning Difficulties: A Review | 10.1109/access.2023.3289496 | IEEE Access |
| R3SE004 | Educational Support for Saudi Students with Learning Disabilities in Higher Education | 10.1111/ldrp.12214 | Sage/Wiley legacy DOI page |
| R3SB021 | Neurodiversity and the Accessible University: Exploring Organizational Barriers, Access Labor and Opportunities for Change | 10.1145/3641011 | ACM Digital Library |
| R3SA006 | Acceptability of the e-authentication in higher education studies: views of students with special educational needs and disabilities | 10.1186/s41239-020-00236-9 | International Journal of Educational Technology in Higher Education / SpringerOpen |
| R3SA018 | AI-Driven Innovation Using Multimodal and Personalized Adaptive Education for Students With Special Needs | 10.1109/access.2025.3560863 | IEEE Access |

### Strongly useful if accessible

| Record ID | Title | DOI |
| --- | --- | --- |
| R3SA031 | Artificial Intelligence and Sensor Technologies the Future of Education Students with and without Intellectual and Developmental Disabilities | 10.56769/ijpn09102 |
| R3SO028 | Beware of metacognitive laziness: Effects of generative artificial intelligence on learning motivation, processes, and performance | 10.1111/bjet.13544 |
| R3SA022 | The Use of Adaptive Learning Technologies in e-Learning for Inclusive Education: A Systematic Review | 10.57125/elij.2024.03.25.05 |

### Optional background only

| Record ID | Title | DOI |
| --- | --- | --- |
| R3SE005 | What next for Universal Design for Learning? A systematic literature review of technology in UDL implementations at second level | 10.1111/bjet.13328 |
| R3SA001/R3SE002 | Teachers' digital competence to assist students with functional diversity | 10.1111/bjet.13151 |
| R3SO027 | Artificial intelligence applications in Latin American higher education: a systematic review | 10.1186/s41239-022-00326-w |

## 5. Meeting-Ready Interpretation

摘要筛选后，最有价值的新增 SEN/SEND 文献集中在三类：

1. **高等教育中的 learning difficulties / SEND support**: R3SB016, R3SE004, R3SA006, R3SB021。
2. **技术和适应性学习支持**: R3SA018, R3SA031, R3SA022。
3. **学习过程与 AI 支持的方法借鉴**: R3SO028。

这意味着组会前的文献补充不需要追求数量，而应该优先拿到上述 5-8 篇正文。它们足够支撑一个清楚的 addendum：SEN/SEND 学生在高等教育中需要的不只是 accommodation，还包括可访问技术、可信的评估系统、组织层面的 access support，以及未来可以结合多模态数据的自适应学习支持。

## 6. Next Step

用户下载 Priority A 全文后，下一步应做全文级 evidence extraction：

1. study context and population;
2. SEN/SEND category or terminology;
3. technology/intervention/support type;
4. outcome or support need identified;
5. relevance to Experiment 1A and eye-tracking MVP;
6. one-sentence meeting takeaway.
