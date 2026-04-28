# 普通笔记本眼动复现 Source Pack

**日期**: 2026-04-28  
**对应 playbook**: `63_webcam_eye_tracking_replication_playbook_20260428.md`  
**目的**: 记录 A007/C007/A008 三篇核心眼动论文与本机可复用资源的可得性，明确下一步复现边界。

## 1. 当前结论

本轮 source tracking 得到一个很有价值的结论：EDM 2025 的 C007 页面可直接读取全文方法细节，并且其讨论部分明确指出 **不应用于诊断或单独标记学生**。这与本项目把目标收窄为 functional learning needs / learning state inference 完全一致。

当前可立即复用的技术参数来自 C007：

- WebGazer 浏览器端采集。
- 354 名 Prolific 参与者，清洗后 332 人、9964 个 paragraph-level instances。
- 40 段阅读文本，每段平均 46 词。
- 每段平均阅读 11.55 秒。
- 阅读过程中 7 次 thought probes。
- 阅读后 10 道多选理解题。
- 24 个特征：9 个 gaze-based，4 个 text-based，2 个 NLP，9 个 interaction-based。
- 数据质量过滤：阅读时间 < 1 秒剔除；gaze count / response time < 5 剔除；缺失 fixation duration 的实例剔除。
- 模型：RF、XGB、Logistic Regression、KNN、Naive Bayes。
- 评估：Cohen's kappa 主指标，AUROC 辅助指标；learner-level stratified 5-fold CV；SMOTE 仅在训练集比较。
- Broad neurodivergence 分类最佳：Logistic Regression without SMOTE，Kappa = 0.14，AUROC = 0.60。

## 2. 核心论文可得性

| ID | 标题 | 状态 | 可用信息 | 阻塞/下一步 |
| --- | --- | --- | --- | --- |
| A007 | Using a Webcam Based Eye-tracker to Understand Students' Thought Patterns and Reading Behaviors in Neurodivergent Classrooms | ACM 页面访问 403；本地无全文 | C007 references 中确认为 LAK23, pp. 453-463；现有摘要卡已记录 N=43、reading + in-situ thought patterns | 需要用户通过机构访问下载 ACM PDF 或补充材料 |
| C007 | Using Webcam-Based Eye Tracking during a Learning Task to Understand Neurodivergence | EDM 2025 页面可读；PDF 链接公开 | 方法、参与者、WebGazer、任务流程、特征工程、模型、指标、结果、限制均可读取 | 可作为本轮 MVP 主模板；建议后续下载 PDF 保存到 `文章全文/` |
| A008 | One Size Does Not Fit All: Considerations when using Webcam-Based Eye Tracking to Models of Neurodivergent Learners' Attention and Comprehension | ACM 页面访问 403；本地无全文 | C007 references 中确认为 LAK 2025, pp. 24-35；现有摘要卡记录 N=354、TUT/comprehension、公平性与分组模型 | 需要用户通过机构访问下载 ACM PDF 或补充材料 |

## 3. C007 可复用方法参数

### 3.1 采集与任务

| 组件 | 原文做法 | 本项目 MVP 建议 |
| --- | --- | --- |
| 采集工具 | WebGazer，浏览器端，仅记录 x/y gaze coordinates，不保存视频 | 采用 WebGazer，默认不保存视频，只导出 gaze/event/probe CSV |
| 环境要求 | 参与者被要求保持良好光照 | MVP 开始页加入光照与坐姿提醒 |
| 校准 | 阅读任务前进行 WebGazer calibration | 先做 9 点校准 + 简单校准质量检查 |
| 阅读材料 | 40 段心理机制/消费者行为文本，每段约 46 词 | 第一版可用 6-10 段短文本，降低 pilot 时长 |
| probe | 阅读中 7 次 thought probes，每次 4 个问题 | 第一版先 3-5 次 probe，每次 1-2 个问题 |
| 理解题 | 10 道多选题 | 第一版 3-5 道多选题 |

### 3.2 可复用特征

| 特征组 | 原文 | MVP 优先级 |
| --- | --- | --- |
| Gaze-based | gaze count, fixation counts, fixation duration mean/std/skew, dispersion | 高；先做 gaze count、dispersion、valid ratio、offscreen ratio |
| Text-based | text response time, word count 等 | 高；阅读时长和字数必须记录 |
| NLP | sentiment, readability | 中；第一版可后补 readability |
| Interaction-based | gaze 与 text/NLP 的交互 | 中；第一版先做 gaze per word、offscreen per word |

### 3.3 数据质量过滤

原文过滤规则可转化为 MVP 规则：

1. `reading_time < 1s` 的段落剔除。
2. `gaze_count / reading_time_seconds < 5` 的段落标记为低质量。
3. fixation 近似失败或 gaze 缺失过多的段落不用于模型，只用于质量报告。

### 3.4 伦理与应用边界

C007 明确警示：

- 模型不适合医学诊断。
- 不应替代经过验证的行为和认知评估。
- 不应被用于诊断原因或单独标记任何学生。
- 应用于教育支持，而非高风险决策。
- 如果未来触发干预，应该 fail soft，即误报也不能对学习造成负面影响。

本项目应直接采用这条边界。

## 4. 本机可复用资源：`eye-track-demo`

同级目录存在 `c:\Users\Quenton\Documents\Github\eye-track-demo`，不是当前仓库的一部分，但可作为分析侧参考。

### 4.1 文件结构

| 文件/目录 | 可复用价值 |
| --- | --- |
| `sample_data.csv` | 可用于验证 scanpath 脚本输入格式 |
| `synthetic_reading_data.csv` | 模拟阅读 gaze 数据，可用于特征提取 smoke test |
| `process_gaze_demo.py` | 已有 scanpath 可视化示例 |
| `generate_and_visualize_reading.py` | 可生成模拟 reading scanpath 和 heatmap |
| `reading_heatmap.png`, `reading_scanpath.png`, `scanpath_demo.png` | 可作为组会“分析输出长什么样”的示例 |
| `data/` | 含 MIT1003 相关数据压缩包；可能适合作为视觉注意 benchmark 参考，不直接等同教育阅读任务 |

### 4.2 局限

`eye-track-demo` 当前更像数据处理和可视化 demo，不是 WebGazer 浏览器采集 demo。它可以复用到：

- gaze CSV 处理；
- scanpath 图；
- heatmap 图；
- synthetic reading data smoke test。

它不能直接完成：

- 摄像头权限申请；
- WebGazer 校准；
- 阅读任务页面；
- probe 与理解题事件记录。

因此，本项目下一步需要新建或补充浏览器端采集页面。

## 5. 推荐 MVP 路线

### 5.1 第一版不要照搬 C007 全规模

C007 的 40 段文本 + 7 次 probe + 10 道理解题适合正式研究，但对本轮组会前 demo 偏重。第一版建议：

- 6-10 段短文本；
- 3 次 thought probe；
- 3-5 道理解题；
- 9 点校准；
- 本地导出 CSV/JSON；
- 不上传数据，不保存视频。

### 5.2 第一版输出

最低输出：

1. `eye_tracking_demo/index.html`: WebGazer 采集 + 阅读任务 + CSV 导出。
2. `eye_tracking_demo/README.md`: 如何运行、隐私边界、数据字段。
3. `eye_tracking_demo/analysis/extract_features.py`: 将 raw gaze CSV 转为 paragraph-level features。
4. `docs/68_eye_tracking_demo_design_20260428.md`: 固化任务流程和字段。

### 5.3 需要用户协助

1. 下载 A007 / A008 ACM 全文。
2. 可选下载 C007 PDF 并保存到 `文章全文/`。
3. 试跑 WebGazer demo 时允许浏览器摄像头权限。
4. 确认第一版阅读材料使用英文还是中文。

## 6. 组会可讲结论

可以这样说：

> 我们已经找到一篇可直接作为复现模板的 EDM 2025 论文。它使用 WebGazer 在普通浏览器中采集 354 名学习者的阅读任务 gaze 数据，并明确指出这种模型不应被用于诊断或单独标记学生，而应服务于个性化学习支持。这正好支持我们把研究目标从“识别 neurodivergent/SEN 身份”调整为“推断任务中的功能性学习需求”。下一步我们会先做小规模 WebGazer MVP，采集 gaze 坐标、阅读时长、probe 和理解题结果，验证普通笔记本路径是否可行。
