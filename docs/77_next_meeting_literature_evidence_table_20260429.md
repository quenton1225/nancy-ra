# Next Meeting Literature Evidence Table

**日期**: 2026-04-29  
**上游文档**: `75_sen_addendum_abstract_screening_20260429.md`, `76_sen_fulltext_evidence_extraction_20260429.md`  
**全文来源**: `文章全文/`  
**用途**: 组会 brief / slides 可直接使用的文献证据表。

## 1. 编号说明

本表暂时沿用用户下载全文时使用的 A/B 编号：A1-A7, B1。原始检索中的 `R3SA/R3SE/R3SB/R3SO` 编号仍保留在 `75` 文档中。组会后可以再统一编号体系；组会前优先保证证据可讲清楚。

## 2. Meeting-Ready Evidence Table

| ID | Citation shorthand | Context / sample | Method | Key finding | How we use it |
| --- | --- | --- | --- | --- | --- |
| A1 | Yenduri et al. (2023), IEEE Access | Students with specific learning difficulties in inclusive higher education | Review of assistive technologies, support tools/projects, challenges and future directions | Assistive technologies can help students with learning difficulties access learning, work at their own pace, participate in academic activities, and reduce barriers in higher education. The review also touches eye movement + ML and multimodal affect recognition as related future directions. | Use as the main bridge between **SEN/SEND wording**, **higher education**, and **technology-enabled support**. |
| A2 | Abed & Shackelford (2020), Learning Disabilities Research & Practice | 22 Saudi higher education students with diagnosed learning disabilities; 16 undergraduate, 6 postgraduate | Exploratory qualitative interview study using phenomenographic analysis | Students reported unmet needs for lecture notes, knowledgeable lecturers, extended assignment/exam time, private testing rooms, review/practice sessions, study skills/time management workshops, proofreading/editing support, and better administrative coordination. | Use as the clearest concrete evidence that higher education students with learning disabilities need practical support services, not just broad inclusion statements. |
| A3 | Borsotti, Begel & Bjorn (2024), PACM HCI / CSCW | 18 neurodivergent computer science students and 8 university employees across 3 Danish universities | Multi-stakeholder qualitative study with semi-structured interviews and document analysis | Students faced structural and attitudinal barriers in the educational environment and disability support system, including assistive technology access barriers, cognitive/physical access barriers, and social access barriers. | Use carefully as evidence about accessible university systems and cognitive/learning access needs. Avoid making `neurodivergent` the external headline term. |
| A4 | Laamanen et al. (2021), International Journal of Educational Technology in Higher Education | 267 SEND students from seven pilot universities in the TeSLA e-assessment project | Survey study on acceptability of sharing personal data for e-authentication | SEND students were broadly positive about e-authentication, but concerns included technology not working and wrong outputs such as false cheating/authorship judgements. | Use as the ethics and acceptability anchor: data-based support tools must be reliable, transparent, and non-punitive. |
| A7 | Fan et al. (2024), British Journal of Educational Technology | 117 university students completing a writing task with AI, human expert, checklist/writing analytics, or no extra support | Randomized experimental study collecting multi-channel learning, performance and motivation data | Different support agents did not change post-task intrinsic motivation, but produced significant differences in self-regulated learning process frequency and sequences. ChatGPT improved essay score but not knowledge gain/transfer and may promote metacognitive laziness. | Use as the method reference for process data and SRL sequence analysis; it supports our idea that gaze/mouse/timing logs may reveal learning-state differences that outcome scores alone miss. |

## 3. Slide-Ready Claims

| Claim | Supporting articles | Suggested wording |
| --- | --- | --- |
| The terminology shift to SEN/SEND is justified. | A1, A2, A4 | The literature supports using school-facing terms such as `students with learning difficulties`, `students with disabilities`, and `SEND` when discussing learning support in higher education. |
| The problem is support need, not diagnosis. | A2, A3, A4 | The key issue is not identifying a student category, but understanding what academic, administrative, accessibility, and technology support is needed in a specific learning context. |
| Technology support must be trustworthy. | A4 | SEND students may accept data-based technologies, but reliability, false judgements, privacy and user trust must be designed into the system from the start. |
| Assistive/adaptive technology is a plausible support route. | A1, B1 | Assistive and adaptive learning technologies can support access, individualization, communication and task completion, but they need to be matched to actual learner needs. |
| Process data can add value beyond final scores. | A7 | Learning process traces can reveal differences in self-regulated learning that are not visible in motivation scores or final performance alone. |

## 4. Evidence Paragraphs for Brief

### 4.1 SEN/SEND and higher education support

A1 and A2 give the strongest SEN/SEND-facing foundation. A1 reviews assistive technologies for students with specific learning difficulties in inclusive higher education, showing that technology can support access, independent work, participation, and future adaptive learning. A2 provides empirical interview evidence from higher education students with learning disabilities, showing concrete unmet needs such as extended time, lecture notes, knowledgeable lecturers, private rooms, review sessions, study skills support, and better administrative coordination.

**Brief sentence**: Students with learning difficulties in higher education need practical academic and administrative support, and assistive technologies are one route for making that support more accessible and individualized.

### 4.2 Accessible university systems

A3 is valuable because it moves beyond individual accommodation and shows that university systems themselves can create barriers. The article identifies assistive technology access barriers, cognitive/physical access barriers, and social access barriers, while also showing that students often perform invisible access labor to make existing systems work.

**Brief sentence**: Support needs are not only located inside the student; they also emerge from university systems, disability service processes, teaching practices, and access to suitable technologies.

### 4.3 Trust and acceptability of data-based tools

A4 is directly relevant to our future data collection design. In a study of 267 SEND students, e-authentication technologies were broadly acceptable, but students were concerned about systems failing or producing wrong outputs such as false cheating judgements. This is a useful warning for our eye-tracking and interaction logging work.

**Brief sentence**: Any data-based learning support tool for SEND students must be framed as support rather than surveillance, with clear consent, transparent interpretation, and safeguards against punitive misuse.

### 4.4 Learning process data as method

A7 is not SEN-specific, but it is methodologically important. It shows that multi-channel process data and self-regulated learning sequences can reveal differences between AI, human, checklist, and no-support conditions, even when motivation scores do not differ. It also warns that AI support can improve short-term task performance while weakening deeper regulation or transfer.

**Brief sentence**: For our project, gaze, mouse, scroll and response timing should be treated as learning-process signals that may help explain support needs, not as direct labels of learner identity.

## 5. Secondary Evidence for Technical Direction

| ID | Use | Caution |
| --- | --- | --- |
| A5 | Supports the idea of multimodal, personalized adaptive education for students with special needs using neural models and XAI. | Population is school-aged 5-18, not higher education; dataset is public/derived and model-oriented. Use for architecture language only. |
| A6 | Supports the rationale for sensor/process data, learning status, cognitive states, and real-time adaptation. | It is explicitly an opinion article, so do not present it as empirical evidence. |
| B1 | Provides a practical taxonomy of adaptive e-learning tools: platforms, adaptive systems, communication tools, assistive technologies. | Review quality and venue strength are weaker than A1; use as background only. |

## 6. Suggested Slide Layout

### Slide title

SEN/SEND Literature Addendum: What the New Full Texts Add

### Slide body

| Evidence cluster | Articles | Takeaway |
| --- | --- | --- |
| Support needs in HE | A1, A2 | Students with learning difficulties need concrete academic and administrative support. |
| Accessible university systems | A3 | Barriers are structural, technological, cognitive/physical and social, not only individual. |
| Trustworthy technology | A4 | Data-based systems must avoid false judgement, opacity and punitive use. |
| Process-data method | A7 | Learning traces can reveal regulation differences that final outcomes miss. |

### Speaker note

The addendum supports a safer framing: this project should not claim to diagnose students. It should investigate whether optional eye-tracking and interaction traces can help infer task-level learning states and support needs, while using SEN/SEND-facing language for external communication.

## 7. One-Minute Meeting Script

> Following the terminology feedback, I reran the search around SEN/SEND and then checked the priority full texts. The strongest new evidence is not about diagnosing students; it is about support needs in higher education. A1 and A2 show that students with learning difficulties need concrete academic and administrative supports, and that assistive technologies can help make support more accessible. A3 adds that university systems themselves create accessibility barriers. A4 is important ethically: SEND students may accept data-based systems, but only if they are reliable and not used punitively. Finally, A7 gives us a method model: process data can show differences in self-regulated learning that final scores alone may miss. So for our eye-tracking demo, the safest framing is learning-state support, not student classification.

## 8. Next Step

**Status update**: The meeting brief has been created as `78_next_meeting_brief_20260429.md`.

Use this table to build the final meeting brief together with:

- `73_eye_tracking_five_sample_comparison_20260428.md`
- `74_next_meeting_remaining_work_plan_20260428.md`
- `76_sen_fulltext_evidence_extraction_20260429.md`

The next likely work item is converting the brief into slides or updating the eye-tracking demo schema.
