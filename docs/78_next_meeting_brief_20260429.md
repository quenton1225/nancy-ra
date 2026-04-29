# 下次组会简报：SEN/SEND 文献补充与普通笔记本眼动 MVP

**日期**: 2026-04-29  
**对应总计划**: `61_next_meeting_dual_deliverable_plan_20260428.md`  
**文献证据表**: `77_next_meeting_literature_evidence_table_20260429.md`  
**眼动五样本对比**: `73_eye_tracking_five_sample_comparison_20260428.md`  
**下一版采集计划**: `79_next_eye_tracking_data_collection_schema_20260429.md`  
**用途**: 下次组会前的 1-2 页中文简报，可直接拆成 slides。

## 1. 一句话结论

我们已经完成组会前两条主线的核心证据：一条是把文献检索和表述从 `neurodivergent` 外部中心转向 `SEN/SEND / learning difficulties / functional support needs`；另一条是完成普通笔记本 WebGazer 阅读任务 MVP，并用 P001-P005 五个样本验证了采集、特征提取和 scanpath 可视化闭环。

当前最稳妥的研究表述是：

> 本项目不试图诊断学生身份，而是探索能否通过任务中的眼动、交互和响应过程信号，推断学生在特定学习任务中的学习状态和功能性支持需求。

## 2. 术语调整

根据导师对术语敏感性的提醒，外部表述建议从 `neurodivergent-centered wording` 调整为：

- `special educational needs` / `SEN`
- `special educational needs and disabilities` / `SEND`
- `students with learning difficulties`
- `students with disabilities`
- `functional learning needs` / `functional support needs`

`neurodivergent` 仍可以作为内部检索词保留，因为 HCI、accessibility 和 learning analytics 文献仍大量使用这个词；但在组会标题、研究问题和对外口径中，不建议把它放在主语位置。

## 3. 文献补充给我们的启发

### 3.1 核心证据

| 证据组 | 文章 | 组会可讲结论 |
| --- | --- | --- |
| 高等教育中的 SEN/SEND 支持需求 | A1, A2 | 有 learning difficulties 的大学生需要具体的学术和行政支持，而不只是宽泛的 inclusion policy。 |
| 大学系统本身的可访问性问题 | A3 | 支持需求不只来自学生个人，也来自学校系统、disability service 流程、教学实践和技术可及性。 |
| 数据化技术必须可信 | A4 | SEND 学生可以接受数据化系统，但前提是系统可靠、透明，并避免误判和惩罚性使用。 |
| 学习过程数据的方法价值 | A7 | 过程数据可以揭示 self-regulated learning 的差异，这些差异可能不会出现在最终分数或动机问卷里。 |

### 3.2 文章级证据

| 编号 | 简写 | 为什么重要 |
| --- | --- | --- |
| A1 | Yenduri et al. (2023), IEEE Access | 综述 inclusive higher education 中 specific learning difficulties 学生的 assistive technologies，是 SEN/SEND 与技术支持之间最直接的桥。 |
| A2 | Abed & Shackelford (2020), Learning Disabilities Research & Practice | 访谈 22 名高等教育中 diagnosed learning disabilities 学生，指出 extended time、lecture notes、了解 LD 的教师和行政协同等具体支持需求。 |
| A3 | Borsotti, Begel & Bjorn (2024), PACM HCI / CSCW | 指出大学环境中的结构性、态度性、技术可及性、认知/物理可及性和社会性障碍；但对外使用时要避免把 `neurodivergent` 作为主标题。 |
| A4 | Laamanen et al. (2021), IJETHE | 调查 267 名 SEND 学生，说明 e-assessment/e-authentication 可以被接受，但学生担心系统失效和错误判定作弊/作者身份。 |
| A7 | Fan et al. (2024), BJET | 随机实验比较 AI、人类专家、checklist/writing analytics 和无支持条件；过程数据与 SRL 序列能揭示最终表现之外的学习差异。 |

### 3.3 谨慎使用的补充文献

| 编号 | 可用处 | 谨慎点 |
| --- | --- | --- |
| A5 | 可作为多模态个性化 adaptive learning 架构参考 | 对象是 5-18 岁学生，不是高等教育；数据是公开/派生数据，不能当作我们场景的实证证明。 |
| A6 | 可作为 sensor/process data、learning status、real-time adaptation 的概念依据 | 明确是 opinion article，不能当作实证结果讲。 |
| B1 | 可作为 adaptive/inclusive e-learning 工具分类背景 | 综述质量和期刊权威性弱于 A1，只适合作背景。 |

## 4. 眼动 MVP 已完成什么

我们搭建了一个基于浏览器和普通笔记本摄像头的 WebGazer 阅读任务 MVP。流程包括：

1. 输入匿名 participant/session 信息；
2. 点击校准点；
3. 阅读短文本；
4. 回答 TUT / thought probe；
5. 回答理解题；
6. 导出 CSV；
7. 用脚本提取 trial-level features 并生成 scanpath 可视化。

这个 MVP 目前适合作为可行性展示，还不能被当作已经验证过的测量工具。

## 5. 五个 pilot 样本结果

### 5.1 原始数据质量

| 样本 | 条件 | gaze rows | 平均采样率 | 整体 offscreen | 理解题正确 |
| --- | --- | ---: | ---: | ---: | --- |
| P001 | 受试者 1 早期基线，正常光照 | 8494 | 50.0Hz | 0.0274 | 3/3 |
| P002 | 受试者 1，戴眼镜并持续转头 | 3419 | 27.4Hz | 0.0140 | 2/3 |
| P003 | 受试者 2，正常光，不戴眼镜，尽量不转头 | 12915 | 49.6Hz | 0.0132 | 2/3 |
| P004 | 受试者 2，略暗/逆光，不戴眼镜，尽量不转头 | 6225 | 50.0Hz | 0.0050 | 2/3 |
| P005 | 受试者 1 严格基线，不戴眼镜，正常光，尽量不转头 | 5614 | 47.6Hz | 0.0082 | 3/3 |

### 5.2 trial-level 汇总

| 样本 | 阅读总时长 | 平均每 trial gaze samples | 平均 offscreen | TUT positive | 平均难度 | 平均熟悉度 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: |
| P001 | 110.4s | 1851.0 | 0.0102 | 1/3 | 4.7 | 3.0 |
| P002 | 89.5s | 792.7 | 0.0067 | 1/3 | 5.3 | 2.7 |
| P003 | 168.9s | 2775.7 | 0.0059 | 3/3 | 4.7 | 2.3 |
| P004 | 97.2s | 1635.7 | 0.0053 | 3/3 | 3.7 | 4.0 |
| P005 | 86.4s | 1352.7 | 0.0033 | 0/3 | 4.0 | 4.0 |

### 5.3 解释

- **P005 是目前最干净的严格正常条件 baseline**：不戴眼镜、正常光照、尽量不转头，平均采样率 47.6Hz，理解题 3/3，TUT 为 0/3。
- **P002 是压力测试**：同一受试者在戴眼镜并持续转头时，平均采样率从 P005 的 47.6Hz 降到 27.4Hz，说明眼镜/头动很可能影响 tracking density。
- **P004 说明略暗/逆光没有直接让 tracking 崩溃**，但目前还不能说光照没有影响，因为缺少更系统的条件记录。
- **五个样本都完成了完整闭环**：raw CSV、trial-level features 和 scanpath visualizations 都已生成。

## 6. 文献与 pilot 的整合判断

| 问题 | 当前回答 |
| --- | --- |
| 项目是否应当诊断学生类别？ | 不应当。更安全的定位是任务层面的学习状态和支持需求。 |
| SEN/SEND 是否更适合外部表述？ | 是。全文文献支持使用 SEN/SEND、learning difficulties、students with disabilities 和 functional support needs。 |
| 普通笔记本 webcam eye tracking 是否足够做 pilot demo？ | 足够。五个样本都完成任务，四个样本接近 48-50Hz。 |
| 只收 gaze 是否足够？ | 不够。解释 gaze 需要光照、眼镜、头动、run order、鼠标/滚动、响应时间、AOI 和校准质量。 |
| 现在是否适合训练模型？ | 不适合。样本量太小，下一步应先升级数据 schema 和做小规模 controlled pilot。 |

## 7. 下一版数据采集重点

下一版优先补 5 类低风险高价值信息：

| 优先级 | 信息 | 目的 |
| ---: | --- | --- |
| 1 | 鼠标 / pointer: `mousemove`, `click`, `pointerdown/up`, 坐标、按钮状态 | 判断阅读定位、犹豫、选项比较和与 gaze 的一致性。 |
| 2 | 滚动 / wheel: scroll 位置、delta、方向 | 解释阅读速度、回看、跳读和长文本浏览行为。 |
| 3 | 响应时间: probe/quiz 从出现到回答的 latency | 比单纯答案更能反映犹豫、负荷和理解难度。 |
| 4 | AOI 区域: 文本区、题目区、选项区、按钮区的位置和大小 | 把裸 gaze 坐标变成“看了哪里”。 |
| 5 | 校准质量: target 坐标、点击坐标、gaze 偏差、quality flag | 判断每轮数据是否可信，避免把校准噪声误读为行为差异。 |

第二层信息包括：采样稳定性、有效 gaze、offscreen、viewport/devicePixelRatio、浏览器/摄像头上下文、疲劳、光线、眼镜、熟悉度、信心和 support preference。

核心原则是：**不收视频、不收截图、不收诊断身份，但把行为上下文补足**。远程 Zoom 实验可在独立同意下录制音视频，作为辅助回看材料，而不是自动进入主数据表。

更完整的数据计划见 `79_next_eye_tracking_data_collection_schema_20260429.md`。

## 8. 建议组会结构

| 页码 | 内容 | 关键信息 |
| ---: | --- | --- |
| 1 | 项目表述更新 | 从身份标签转向 SEN/SEND 和功能性支持需求。 |
| 2 | 文献补充 | A1-A4/A7 支持 support needs、accessible systems、trustworthy technology 和 process data。 |
| 3 | 眼动 MVP | WebGazer 阅读任务、CSV 导出、feature extraction、scanpath。 |
| 4 | 五样本 pilot 表 | 五个样本完整；四个接近 48-50Hz；P002 在眼镜/转头条件下降低。 |
| 5 | pilot 解释 | P005 是最干净 baseline；条件元数据必须补齐。 |
| 6 | 整合结论 | demo 可行，但还不是验证过的测量工具。 |
| 7 | 下一步计划 | 加上下文字段，做 controlled pilot，再分析更丰富的过程信号。 |

## 9. 一分钟口头稿

> 根据导师关于术语的提醒，我把文献检索和表述从 neurodivergent 外部中心转向 SEN/SEND、students with learning difficulties 和 functional support needs。新下载的全文说明，核心问题不是诊断学生，而是理解学生在高等教育中需要什么支持。A1 和 A2 支持 assistive technology 和学术支持需求，A3 说明大学系统本身会制造可访问性障碍，A4 提醒我们数据化系统必须可靠、透明、不能惩罚性使用，A7 则说明过程数据可以揭示最终分数看不到的学习调节差异。与此同时，我搭建了 WebGazer 阅读任务 MVP，并收集了五个样本。五个样本都完成了 raw CSV、features 和 scanpath；P005 是目前最干净的正常条件 baseline，P002 显示眼镜和转头会降低采样密度。因此我建议下一步把 demo 当作 feasibility proof，先升级数据 schema，补鼠标、滚动、响应时间、AOI、校准质量、光照、眼镜和坐姿等上下文，再做小规模 controlled pilot。

## 10. 希望导师组确认的问题

> 下一阶段是否可以将研究重点定位为：在 SEN/SEND / functional support needs 的外部表述下，使用普通笔记本 webcam eye tracking 和交互日志，探索任务层面的学习状态与支持需求？

如果可以，下一份 deliverable 应该是 revised data collection protocol + richer-context pilot，而不是马上训练模型。
