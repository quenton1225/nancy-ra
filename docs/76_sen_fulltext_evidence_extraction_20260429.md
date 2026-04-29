# SEN/SEND Full-Text Evidence Extraction

**日期**: 2026-04-29  
**对应摘要筛选**: `75_sen_addendum_abstract_screening_20260429.md`  
**全文来源**: `文章全文/`  
**范围**: A1-A7, B1  
**目的**: 读取用户下载的全文，判断哪些文章可进入组会证据包，哪些只能作为背景或方法参考。

## 1. 总体判断

| 编号 | 文章角色 | 全文级判断 | 组会用途 |
| --- | --- | --- | --- |
| A1 | Assistive technologies in inclusive higher education review | **核心纳入** | SEN/SEND 技术支持主证据 |
| A2 | Higher education LD support needs interview study | **核心纳入** | 支持需求和 accommodation 缺口主证据 |
| A3 | Accessible university / neurodivergent access barriers qualitative study | **核心纳入，但对外换术语** | 大学组织障碍、access labor、支持系统缺口 |
| A4 | SEND students' views on e-authentication in HE | **核心纳入** | 技术系统可接受性、信任、误判风险 |
| A5 | Multimodal adaptive education for special needs | **方法/未来路线纳入，谨慎使用** | 支持多模态 adaptive learning 方向，不作为 HE 实证 |
| A6 | AI and sensor technologies opinion paper | **概念背景纳入，弱证据** | 支撑 real-time process data / sensor rationale |
| A7 | GenAI, SRL process data, metacognitive laziness experiment | **方法论纳入** | 支撑学习过程数据、SRL 序列、AI 支持风险 |
| B1 | Adaptive e-learning technologies for inclusive education review | **背景纳入，谨慎使用** | 工具类别和 inclusive e-learning 背景 |

最适合组会主线的组合是 A1 + A2 + A3 + A4。A5-A7/B1 可以放在“下一步技术路线和方法借鉴”里，不建议和 A1-A4 混成同等强度证据。

## 2. Full-Text Extraction Table

| ID | File | Study type | Population/context | Key evidence | Relevance to our project | Decision |
| --- | --- | --- | --- | --- | --- | --- |
| A1 | `A1. From Assistive Technologies to Metaverse - Technologies in Inclusive Higher Education for Students With Specific Learning Difficulties.pdf` | Review | Students with specific learning difficulties in inclusive higher education | Assistive technology can enhance/maintain/improve capacities; review covers learning difficulty types, support tools/projects, challenges and future directions. It also mentions eye movement + ML for dyslexia screening and multimodal affect recognition for learners with intellectual disabilities/autism. | Strong bridge between SEN/SEND terminology, higher education, assistive/adaptive technologies, and our eye-tracking/multimodal direction. | **Keep as core evidence** |
| A2 | `A2. Educational Support for Saudi Students with Learning Disabilities in Higher Education.pdf` | Exploratory qualitative interview; phenomenographic analysis | 22 Saudi HE students with diagnosed learning disabilities; 16 undergraduate and 6 postgraduate | Students reported unmet needs for lecture notes/handouts, knowledgeable lecturers, extended assignment/exam time, private testing rooms, review/practice sessions, study skills/time management workshops, proofreading/editing, and better administrative coordination. | Direct evidence that HE students with LD need concrete academic and administrative supports, not only generic inclusion policy. Useful for defining support needs before proposing AI/eye-tracking tools. | **Keep as core evidence** |
| A3 | `A3. Neurodiversity and the Accessible University.pdf` | Exploratory qualitative multi-stakeholder study; interviews + document analysis | 18 neurodivergent CS students and 8 university employees across 3 Danish universities | Identifies structural and attitudinal barriers in educational environments and disability support systems: assistive technology access barriers, cognitive/physical access barriers, and social access barriers. Introduces access labor and access grafting. | Very strong for organizational support needs in university settings. Because the project wants to externally emphasize SEN/SEND, cite it carefully as evidence about accessible university and students with cognitive/learning access needs. | **Keep as core evidence, wording-sensitive** |
| A4 | `A4. Acceptability of the e-authentication in higher education studies.pdf` | Survey study in TeSLA e-assessment project | 267 SEND students from seven pilot universities | Research questions cover acceptability of sharing personal data for e-authentication, influence of SEND/background variables, and perceived advantages/disadvantages. Findings suggest broadly positive acceptability, but key concerns include technology not working and wrong cheating/authorship outputs. | Important counterweight: technology for SEND students must be reliable, transparent, and not punitive. Directly relevant to our future gaze/mouse/context logging and consent framing. | **Keep as core evidence** |
| A5 | `A5. AI-Driven_Innovation_Using_Multimodal_and_Personalized_Adaptive_Education_for_Students_With_Special_Needs.pdf` | ML/DL modelling paper | Dataset built from publicly available NCES-related disability data; school-aged learners 5-18, not HE | Trains multiple neural architectures on multimodal-like features; uses transformer/attention models and XAI; uses SMOTE balancing. Data are not our HE context and may be more synthetic/model-demonstration than field intervention. | Useful to justify a future multimodal adaptive learning pipeline, but not strong evidence for HE SEN students or real-world classroom deployment. | **Keep as future-method evidence, use cautiously** |
| A6 | `A6. Artificial Intelligence and Sensor Technologies the Future of Individualized and Differentated Education.pdf` | Opinion/concept paper | Special education; developmental/intellectual disabilities; classroom/online systems | Argues sensor technologies, neurotechnologies, physiological signal processing and AI can assess learning status/cognitive states in real time and support just-in-time adaptation. Explicitly labeled as opinion. | Good conceptual support for why eye-tracking/process data can matter, but weak as empirical evidence. Do not overclaim. | **Use as conceptual background only** |
| A7 | `A7. Brit J Educational Tech - 2024 - Fan - Beware of metacognitive laziness  Effects of generative artificial intelligence on.pdf` | Randomized experimental study | 117 university students; AI vs human expert vs checklist/writing analytics vs no extra tool on writing task | Collects multi-channel learning, performance and motivation data; finds no post-task intrinsic motivation difference, but significant differences in self-regulated learning process frequency/sequences. ChatGPT improves essay score but not knowledge gain/transfer, and may promote technology dependence/metacognitive laziness. | Strong method reference for process data, SRL sequence analysis, and caution around AI support. Not SEN-specific. | **Keep as method/risk evidence** |
| B1 | `B1. The Use of Adaptive Learning Technologies in e-Learning for Inclusive Education Gevorgyan,+S.++(2024).pdf` | Systematic review-style paper using PRISMA | Inclusive education and adaptive e-learning; Scopus/Google Scholar; 45 selected sources | Identifies e-learning platforms, adaptive systems, communication tools and assistive technologies as important for supporting students with SEN. Discusses individualized/differentiated learning, co-teaching, Read&Write, Kurzweil 3000, Dragon NaturallySpeaking. | Useful for a practical taxonomy of adaptive/inclusive e-learning tools. Venue/method quality is weaker than A1/A7; use as background, not central authority. | **Use as background only** |

## 3. What Changed After Reading Full Texts

### 3.1 Stronger than abstract suggested

- **A2** is more valuable than it looked from abstract alone because it gives concrete support measures requested by students with LD in higher education.
- **A4** is also stronger after full text because it directly addresses SEND students' attitudes to data-sharing technology in assessment contexts; this is useful for ethics and acceptability of our future multimodal logging.

### 3.2 Needs more caution than abstract suggested

- **A5** sounds very close to our multimodal direction, but its population is school-aged learners aged 5-18 and the dataset is constructed from public/derived data rather than our target higher education setting. Use it for architecture language, not for claims about HE students.
- **A6** is explicitly an opinion article. It is useful for rationale but should not be presented as empirical evidence.
- **B1** is useful as a tool taxonomy, but its review quality and venue strength are weaker than A1.

### 3.3 Wording-sensitive article

- **A3** uses `neurodiversity/neurodivergent`, which the user noted may be sensitive in the school context. The article is still highly relevant, but in slides we should frame it as evidence about **accessible university environments, cognitive/learning access needs, and disability support systems**, rather than making neurodivergence the headline term.

## 4. Recommended Evidence Set for Meeting

### 4.1 Core SEN/SEND and higher education support evidence

| Use | Articles | Claim supported |
| --- | --- | --- |
| Support needs in HE | A2, A3 | Students with LD/SEN-like needs face concrete academic, administrative and organizational barriers in university settings. |
| Technology-enabled support | A1, A4 | Assistive technologies can support access and learning, but technical systems must be acceptable, reliable and non-punitive. |
| Wording bridge | A1, A2, A4 | External wording can center `SEN/SEND`, `students with learning difficulties`, `students with disabilities`, and `functional learning needs`. |

### 4.2 Technical route and method evidence

| Use | Articles | Claim supported |
| --- | --- | --- |
| Multimodal adaptive direction | A5, A6 | Future systems can combine academic, behavioral, environmental and sensor/process data to adapt support, but empirical validation is still needed. |
| Learning process analytics | A7 | Process data and SRL sequences can reveal differences that outcome scores or motivation scales alone miss. |
| Tool taxonomy | B1 | Adaptive e-learning support includes platforms, adaptive systems, communication tools and assistive technologies. |

## 5. Suggested Slide Language

### 5.1 Literature addendum takeaway

> The SEN/SEND addendum confirms that the project should not frame technology as a diagnostic tool. In higher education, students with learning difficulties and SEND-related needs require concrete academic support, accessible institutional processes, and trustworthy technologies. Eye-tracking and interaction data should therefore be positioned as optional signals for learning-state support, not as labels of disability.

### 5.2 Evidence map sentence

> A1 and A2 support the need for assistive and educational support in higher education; A3 shows organizational access barriers in universities; A4 highlights SEND students' concerns and acceptance conditions for data-based assessment technologies; A7 gives a method model for using process data to study learning regulation.

## 6. Next Extraction Step

**Status update**: This step has been completed as `77_next_meeting_literature_evidence_table_20260429.md`.

Before building the final meeting brief, use `77_next_meeting_literature_evidence_table_20260429.md` as the compact evidence table. It extracts one paragraph each from A1-A4/A7 and includes:

1. citation;
2. participant/context;
3. method;
4. key finding;
5. one-sentence relevance to Experiment 1A;
6. slide-ready wording.

The next likely document is `78_next_meeting_brief_20260429.md`.
