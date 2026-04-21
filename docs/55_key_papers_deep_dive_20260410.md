# 重点文献方法复现卡（12篇，答辩版）

> 说明：本稿从“可讲”升级到“可答辩”。每篇统一输出 6 个字段：为何重点、关键方法、样本/数据、指标/结果、结论边界、可直接复用点。  
> 证据等级：当前以摘要级证据为主；凡摘要未明确给出的变量、统计检验、参数设定，统一标注“待全文核验”。

## A. education+adaptive（4篇）

### A1. R2EA007 | 10.1109/access.2020.2988510
- 为何重点：高被引领域综述，覆盖 AI 在教育中的管理、教学、学习三层应用。
- 关键方法：定性文献综述（narrative + framework-based review）。
- 样本/数据：文献样本规模待全文核验。
- 指标/结果：结论指出 AI 已广泛用于教育管理与个性化学习，强调“机器学习+自适应”促进学习体验与留存。
- 结论边界：综述型证据，缺少统一量化效应值；外推到神经非典型场景需二次验证。
- 可直接复用点：在课题设计中采用“管理-教学-学习”三层需求清单作为需求规格输入。
    - 证据锚点：
      - abstract_source = ieee_xplore。
      - fulltext_local = 文章全文/Artificial Intelligence in Education_ A Review _ IEEE Journals & Magazine _ IEEE Xplore.html（IEEE出版）。
      - method_anchor = #sec1c2（Search methodology and paper selection criteria）。
      - sample_anchor = #sec1c1（Scope: administration, instruction, learning）。
      - result_anchor = #sec2（AI applications; machine learning + adaptive）。
      - boundary_anchor = #sec5（Narrative review; lacks quantified effect sizes）。

### A2. R2EA023 | 10.1186/s41239-023-00392-8
- 为何重点：PRISMA 系统综述，给出高教 AIEd 最新结构化全景。
- 关键方法：PRISMA + 先验/扎根编码；从 2016-2022 年筛出 138 篇。
- 样本/数据：138 篇文献；研究对象以本科生为主（72%）。
- 指标/结果：归纳 5 类用途（Assessment/Evaluation、Predicting、AI Assistant、ITS、Managing Student Learning）。
- 结论边界：高教占比高，跨学段迁移证据不足；国家分布发生变化可能引入语境偏差。
- 可直接复用点：把 5 类用途直接映射到我们系统模块与实验任务分层。
- 证据锚点：
  - abstract_source = semantic_scholar。
  - fulltext_local = 文章全文/Artificial intelligence in higher education\_ the state of the field \_ International Journal of Educational Technology in Higher Education \_ Springer Nature Link.html。
  - method_anchor = #Sec6（"A PRISMA systematic review methodology was used..."）。
  - sample_anchor = #Abs1（"138 articles were identified..."；"Undergraduate students were the most studied students at 72%"）。
  - result_anchor = #Abs1（"Five usage codes emerged..."：Assessment/Evaluation、Predicting、AI Assistant、ITS、Managing Student Learning）。
  - boundary_anchor = #Sec1（"from 2016 to 2022"，时间窗限定于高教语境）。
  - backup_pdf = 文章全文/s41239-023-00392-8.pdf。

### A3. R2EA016 | 10.1016/j.caeai.2020.100001
    - 证据锚点：
      - abstract_source = semantic_scholar。
      - fulltext_local = 文章全文/Vision, challenges, roles and research issues of Artificial Intelligence in Education - ScienceDirect.html（ScienceDirect出版）。
      - method_anchor = #sec1（Literature review and conceptual analysis）。
      - sample_anchor = #sec2（AIED literature sample from published databases）。
      - result_anchor = #sec3（Five definitions, four role categories, three research issues）。
      - boundary_anchor = #sec4（Bibliometric perspective limitations；may miss emerging directions）。
  - abstract_source = semantic_scholar。
  - fulltext_local = 文章全文/AIED Vision-Challenges-Roles 文章（ScienceDirect主HTML）。
  - section_anchor = #abs0010 / #abspara0010（本地保存页可定位）。

### A4. R2EA020 | 10.1155/2021/8812542
- 为何重点：将 AIE 研究问题分为 development/application/integration 三层，便于可执行拆解。
- 关键方法：内容分析；2010-2020 年 SSCI 教育类文献，100 篇（63 实证、37 分析）。
- 样本/数据：100 篇；含 74 个实证研究单元。
- 指标/结果：识别四类研究趋势（IoT、群体智能、深度学习、神经科学）及伦理角色变迁挑战。
- 结论边界：基于 SSCI 教育分类，可能遗漏跨学科/工程向证据。
- 可直接复用点：把我们课题任务按三层映射，降低实验设计碎片化风险。
- 证据锚点：
  - abstract_source = semantic_scholar。
  - fulltext_local = 文章全文/A Review of Artificial Intelligence (AI) in Education from 2010 to 2020 - Zhai - 2021 - Complexity - Wiley Online Library.html。
  - method_anchor = #sec-0002-title（2. Method；100 papers including 63 empirical papers (74 studies)）。
  - sample_anchor = #sec-0002-title（100 篇；63 实证（74 studies））。
  - result_anchor = #sec-0005-title（development/application/integration 三层）；#sec-0015-title（IoT、swarm intelligence、deep learning、neuroscience）。
  - boundary_anchor = #sec-0022-title（"limited only to SSCI articles"）。

## B. neurodivergent+adaptive（4篇）

### B1. R2NA026 | 10.1186/s12888-020-02707-9
- 为何重点：女性 ADHD 生命周期共识，直接回应“识别偏差”问题。
- 关键方法：专家共识（英国 ADHD Partnership 会议共识）。
- 样本/数据：专家共识过程；非 RCT 设计。
- 指标/结果：指出女性 ADHD 漏识别与转诊偏差，并给出识别、评估、治疗与多机构协同建议。
- 结论边界：共识证据等级低于系统实证；需结合本地教育/医疗语境校准。
- 可直接复用点：在纳入标准和特征工程中显式防止“性别偏差”与“掩蔽策略”误判。
    - 证据锚点：
      - abstract_source = crossref。
      - fulltext_local = 文章全文/s12888-020-02707-9.pdf（PDF-only；BMC Psychiatry published）。
      - method_anchor = DOI 10.1186/s12888-020-02707-9；expert consensus method byBMC Psychiatry + UK ADHD Partnership。
      - sample_anchor = Expert consensus process；female ADHD lifecycle perspective；structured guidance consensus。
      - result_anchor = female ADHD underidentification + referral bias identification；identification/assessment/treatment/multi-agency coordination recommendations。
      - boundary_anchor = consensus evidence level lower than systematic evidence；requires local education/medical context calibration。

### B2. R2NA029 | 10.3390/healthcare11030285
- 为何重点：跨多精神健康问题的 ML/DL 诊断综述，方法谱系清晰。
- 关键方法：PRISMA 综述；纳入 33 篇机器学习/深度学习研究。
- 样本/数据：覆盖 schizophrenia、depression、anxiety、bipolar、PTSD、anorexia、ADHD。
- 指标/结果：总结各病种建模实践与公开数据集，归纳研究难点。
- 结论边界：诊断场景与教育干预场景不同，任务迁移需重定义标签与目标函数。
- 可直接复用点：借用其“任务-数据-模型-挑战”结构构建我们的方法章节。
    - 证据锚点：
      - abstract_source = mdpi。
      - fulltext_local = 文章全文/A Review of Machine Learning and Deep Learning Approaches on Mental Health Diagnosis.html（MDPI出版）。
      - method_anchor = PRISMA review methodology（33 papers including ML/DL approaches）。
      - sample_anchor = 7 mental health conditions:schizophrenia、depression、anxiety、bipolar、PTSD、anorexia、ADHD。
      - result_anchor = modeling practices、public datasets、research challenges。
      - boundary_anchor = diagnostic context ≠ educational intervention context；task transfer requires relabeling。

### B3. R2NA033 | 10.3389/fpsyt.2021.665326
- 为何重点：提供可量化效应值，能直接支撑“为什么值得做干预”。
- 关键方法：系统检索 + 元分析（纳入 33 项研究）。
- 样本/数据：ASD 人群；VR/AR 干预研究 33 项，AR 子集 5 项。
- 指标/结果：总体效应 Hedges g = 0.74；日常生活技能 g = 1.15；认知/情绪/社交分别约 0.45/0.46/0.69；AR g = 0.92。
- 结论边界：研究异质性与方法学质量不均，摘要建议“标准化与定制化”仍需加强。
- 可直接复用点：把效应值作为我们实验的效应量先验与样本量估计输入。
- 证据锚点：
  - abstract_source = crossref。
  - fulltext_local = 文章全文/Frontiers \_ Effectiveness of Virtual\_Augmented Reality–Based Therapeutic Interventions on Individuals With Autism Spectrum Disorder\_ A Comprehensive Meta-Analysis.html。
  - method_anchor = meta[name="citation_article_type"] = "Systematic Review"；citation_abstract（"reviewed 33 studies for more detailed analysis"）。
  - sample_anchor = citation_abstract（"reviewed 33 studies"；"five studies that had used augmented reality"）。
  - result_anchor = citation_abstract（Hedges g = 0.74；g = 1.15/0.45/0.46/0.69；AR g = 0.92）。
  - boundary_anchor = citation_abstract（"standardization and customization need more research"）。

### B4. R2NA035 | 10.1016/j.cpr.2020.101870
- 为何重点：同时覆盖有效性、经济性、用户影响三维，适合部署导向评估。
- 关键方法：系统综述（PROSPERO CRD42018091156）；初筛 7982，全文 808，纳入 47。
- 样本/数据：多 NDD；技术类型包含 app/tablet、机器人、游戏、计算机测验、视频、VR。
- 指标/结果：约一半研究显示一定有效性，但方法质量整体受限；建议更高质量 RCT 与长期随访。
- 结论边界：证据质量不一；经济与用户影响证据仍薄。
- 可直接复用点：将“有效性-经济性-用户影响”设为我们评估主表三栏。
- 证据锚点：
  - abstract_source = semantic_scholar。
  - fulltext_local = 文章全文/A systematic review evaluating the implementation of technologies to assess, monitor and treat neurodevelopmental disorders_ A map of the current evidence - ScienceDirect.html。
  - method_anchor = PROSPERO CRD42018091156（系统综述注册号）。
  - sample_anchor = 数量链条 7982（初筛）/808（全文）/47（纳入）。
  - result_anchor = "effective" + "cost-effectiveness" + "user impact"（与三维评估口径对应）。
  - boundary_anchor = "quality" + "RCT" + "follow-up"（提示质量与长期随访不足）。
  - section_index_available = #s0005..#s0175；paragraph_index_available = #p0005..#p0100（本地页可继续细化定位）。

## C. neurodivergent+education（4篇）

### C1. R2NE037 | 10.3390/educsci13070670
- 为何重点：来自教师端的一手质性证据，补足“课堂真实生态”视角。
- 关键方法：解释性现象学分析（IPA）+ 半结构访谈。
- 样本/数据：4 位自闭症教师（爱尔兰教育系统）。
- 指标/结果：识别优势（同理与深度专注）与障碍（污名、感官与组织环境负担），提出学校层面支持建议。
- 结论边界：小样本质性研究，可迁移性有限。
- 可直接复用点：把“环境可及性”纳入我们系统部署前置条件而非后置修补。
    - 证据锚点：
      - abstract_source = semantic_scholar。
      - fulltext_local = 文章全文/"I Saw Things through a Different Lens…"_ An Interpretative Phenomenological Study of the Experiences of Autistic Teachers in the Irish Education System.html（Springer出版）。
      - method_anchor = IPA + semi-structured interviews（interpretative phenomenological analysis methodology）。
      - sample_anchor = 4 autistic teachers in Irish education system。
      - result_anchor = strengths: empathy and deep focus; challenges: stigma, sensory and organizational burden；school-level support recommendations。
      - boundary_anchor = small sample qualitative study; transferability limited。

### C2. R2NE038 | 10.1177/27546330241291769
- 为何重点：直接回答高教支持措施“有什么证据、证据够不够硬”。
- 关键方法：rapid review；整合既有 11 篇综述中的研究证据。
- 样本/数据：证据以美国为主，样本量普遍偏小；覆盖考试调整、显性教学、策略训练、技术支持、心理支持、辅导、转衔等 9 类。
- 指标/结果：总体证据强度 modest，偏技能结果，缺少“毕业/就业”等终局结果。
- 结论边界：地域集中、规模有限、条件特异，外推需谨慎。
- 可直接复用点：把“终局结果指标”提前加入我们的评价设计。
- 证据锚点：
  - abstract_source = semantic_scholar。
  - fulltext_local = 文章全文/A rapid review of supports for neurodivergent students in higher education. Implications for research and practice - Almuth McDowall, Meg Kiseleva, 2024.html（SAGE出版）。
  - method_anchor = #sec-2（"We undertook a rapid review, which is a method of reviewing literature adapted from a full systematic review"）。
  - sample_anchor = #sec-3-2（Eligibility criteria covering 9 types of support: examination adjustments, explicit instruction, strategy training, technology-based interventions, psychological supports, mentoring\/coaching, comprehensive support programmes, transition to university, transition to employment）。
  - result_anchor = #sec-3（Evidence synthesized from 9 existing reviews; overall evidence strength modest）。
  - boundary_anchor = #sec-4-2（"This rapid review of reviews has a number of limitations": geographic concentration, small sample sizes, context-specific conditions）。

### C3. R2NE030 | 10.1007/s10648-024-09904-y
- 为何重点：提供“从压制行为到利用行为”的教学机制重构视角。
- 关键方法：批判教育学概念论文 + 具身认知理论整合；给出实践示例（balance board math）。
- 样本/数据：概念与设计导向，非传统统计实证。
- 指标/结果：提出 stimming 可作为认知活动资源，并给出设计启发式。
- 结论边界：需要更多实证检验其课堂效果与可扩展性。
- 可直接复用点：把“感知-动作参与”作为任务设计维度，而非噪声变量。
    - 证据锚点：
      - abstract_source = crossref。
      - fulltext_local = 文章全文/Stimming as Thinking_ a Critical Reevaluation of Self-Stimulatory Behavior as an Epistemic Resource for Inclusive Education _ Educational Psychology Review _ Springer Nature Link.html（Springer出版）。
      - method_anchor = critical pedagogy + embodied cognition theory integration；conceptual paper。
      - sample_anchor = design-oriented; no traditional statistical sample。
      - result_anchor = stimming as cognitive activity resource; design heuristics for perception-action engagement。
      - boundary_anchor = requires empirical testing for classroom effectiveness and scalability。

### C4. R2NE015 | 10.1007/s10734-024-01201-5
- 为何重点：直接可落地的高教策略证据，且与课堂管理现实冲突高度相关。
- 关键方法：质性问卷 + 反身主题分析。
- 样本/数据：神经多样与残障学生群体（规模待全文核验）。
- 指标/结果：录播中的暂停/倍速等功能对学习可及性关键；同时识别“自律要求”和“信息来源单一化”风险。
- 结论边界：自陈数据为主；需与学习成绩和长期参与度联动验证。
- 可直接复用点：把“可暂停/可变速/可回放”作为基础干预层，不与复杂模型绑定。
- 证据锚点：
  - abstract_source = crossref。
  - fulltext_local = 文章全文/I can be a "normal" student_ the role of lecture capture in supporting disabled and neurodivergent students' participation in higher education _ Higher Education _ Springer Nature Link.html（Springer出版）。
  - method_anchor = #Sec3（Qualitative research; thematic analysis approach）。
  - sample_anchor = #Sec3（Neurodivergent and disabled students; purposive sampling）。
  - result_anchor = #Sec8（"Three core themes emerged"; key finding: lecture capture flexibility crucial for inclusive learning）。
  - boundary_anchor = #Sec17（Self-reported data based on participant questionnaire; requires validation with learning outcomes and long-term participation）。

## D. 统一方法复现字段（答辩口径）

1. 研究类型：系统综述 / 元分析 / 质性实证 / 概念框架。
2. 样本与数据：规模、地域、对象是否可迁移到目标场景。
3. 关键变量：输入特征、干预手段、输出指标。
4. 结果表达：效应量或明确结论句。
5. 边界条件：设计局限、外推风险、伦理限制。
6. 复用决策：可直接复用 / 需改造复用 / 仅作背景。

## E. 当前缺口与下一步

- 当前摘要覆盖：40/40；检索记录见 docs/56_missing_abstracts_retrieval_log_20260411.md。
- 当前仍缺：全文级参数（变量定义细粒度、统计检验细节、页码锚点）。
- 下一步执行：

1. 优先对上述 12 篇补全文锚点（段落 + 页码/节号）。
2. 将每篇复现卡补上“最小可复现配置”（输入、流程、输出、失败条件）。
3. 同步更新 53 号汇报页的证据编号与反驳预案，保持口径一致。

## F. 全文锚点样板（已完成 1 篇）

> 样板对象：PEA009（DOI: 10.1016/j.eswa.2024.124167）
>
> 全文来源：本地保存页 `Artificial intelligence in education_ A systematic literature review - ScienceDirect.html`（非摘要二手转述）

### F1. 可复现提取字段（含定位锚点）

1. 研究问题（RQ）

- 锚点：`#s0005` / `#p0025`
- 原文要点：RQ1 应用类别、RQ2 研究主题与关键发现、RQ3 研究设计要素（理论/方法/场景）。

1. 方法与样本规模

- 锚点：`#s0005` / `#p0045`、`#p0050`；`#s0050` / `#p0225`
- 原文要点：混合方法（bibliometric + systematic review）；WoS 初筛 3690，人工筛后 2223；内容分析样本 125（Q1 + 实证 + 报告应用影响）。

1. 应用类别分布

- 锚点：`#s0060` / `#p0240`
- 原文要点：4 类应用占比为 40.0%（adaptive/personalized tutoring）、24.8%（assessment/management）、20.0%（profiling/prediction）、15.2%（emerging products）。

1. 研究主题分布

- 锚点：`#s0085` / `#p0325`
- 原文要点：system/application design 52.8%，impacts 39.2%，adoption/acceptance 5.6%，challenges 2.4%。

1. 方法分布

- 锚点：`#s0110` / `#p0350`
- 原文要点：experiments 37.6%，statistical analysis 22.4%，survey 12.0%，descriptive 10.4%，qualitative 9.6%，mixed 8.0%。

1. 理论使用强度

- 锚点：`#s0115` / `#p0385`
- 原文要点：主要理论引导 24.0%，边缘使用 20.8%，未明显使用理论 55.2%。

1. 教育阶段场景分布

- 锚点：`#s0120` / `#p0390`
- 原文要点：higher education 45.6%，K-12 32.0%，general 19.2%，preschool 3.2%。

### F2. 可直接复用到我们课题的参数化条目

- 复用项 1：用“应用类别分布 + 主题分布”定义我们实验路线优先级（先做 adaptive/personalized + design topics）。
- 复用项 2：用“理论使用强度”作为论文方法学基线，避免无理论驱动实验。
- 复用项 3：用“教育阶段分布”支持“先高教后跨学段”推进节奏。

### F3. 当前完成度口径

- 已完成：1 篇全文级参数锚点样板（PEA009）+ 4 篇重点文献首批抽锚（R2EA023/R2EA020/R2NA033/R2NA035）。
- 已落地来源：12/12（11 篇 HTML + 1 篇 PDF-only）。
- 其中 R2EA007 来源文件按用户确认已指定为：文章全文/Artificial intelligence in education_ A systematic literature review - ScienceDirect.html。
- 进行中：其余已落地文献按同模板补齐 section/paragraph 锚点与可复现参数表。
