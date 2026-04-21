# 全文锚点补齐进度表（12篇重点）

## 口径

- 目标：将 12 篇重点文献从“摘要级可讲”升级为“全文级可复现”。
- 判定标准：每篇至少补齐 `方法`、`样本/数据`、`指标/结果`、`边界` 四类字段，且带 section/paragraph 或页码锚点。
        - 当前状态：✅ 已完成 1 篇样板（PEA009）+ 完整 12 篇重点文献全部首批锚点补齐。

## 进度总览

| record_id | doi | 状态 | 全文来源 | 锚点完成度 | 备注 |
| --- | --- | --- | --- | --- | --- |
    | R2EA007 | 10.1109/access.2020.2988510 | 已完成首批锚点 | HTML（IEEE Xplore） | 4/4 | 已补 sec1c1/sec2/sec5 管理/教学/学习锚点 |
| R2EA023 | 10.1186/s41239-023-00392-8 | 已完成首批锚点 | HTML + PDF（Springer页 + s41239-023-00392-8.pdf） | 4/4 | 已补 Sec6/Abs1 及 5 类用途锚点 |
    | R2EA016 | 10.1016/j.caeai.2020.100001 | 已完成首批锚点 | HTML（ScienceDirect） | 4/4 | 已补 sec1-4 AIED 定义与角色 |
| R2EA020 | 10.1155/2021/8812542 | 已完成首批锚点 | HTML（A Review of AI in Education 2010-2020 - Wiley） | 4/4 | 已补 sec-0002/sec-0005/sec-0022 锚点 |
        | R2NA026 | 10.1186/s12888-020-02707-9 | 已完成首批锚点 | PDF（BMC Psychiatry） | 4/4 | 已补 DOI + 女性ADHD共识锚点 |
        | R2NA029 | 10.3390/healthcare11030285 | 已完成首批锚点 | HTML（MDPI） | 4/4 | 已补 PRISMA + 7 疾病 ML/DL 建模 |
| R2NA033 | 10.3389/fpsyt.2021.665326 | 已完成首批锚点 | HTML（Frontiers Meta-Analysis页） | 4/4 | 已补 g 值与标准化/定制化边界锚点 |
| R2NA035 | 10.1016/j.cpr.2020.101870 | 已完成首批锚点 | HTML（A map of the current evidence - ScienceDirect） | 4/4 | 已补 PROSPERO 与 7982/808/47 数量链条锚点 |
        | R2NE037 | 10.3390/educsci13070670 | 已完成首批锚点 | HTML（Springer） | 4/4 | 已补 IPA + 4 自闭症教师样本 |
| R2NE038 | 10.1177/27546330241291769 | 已完成首批锚点 | HTML（A rapid review of supports...） | 4/4 | 已补 sec-2/3/4 及 9 类支持锚点 |
        | R2NE030 | 10.1007/s10648-024-09904-y | 已完成首批锚点 | HTML（Springer） | 4/4 | 已补批判教育学+具身认知 |
| R2NE015 | 10.1007/s10734-024-01201-5 | 已完成首批锚点 | HTML（I can be a normal student） | 4/4 | 已补 Sec3/8 及三核心主题锚点 |

## 已完成样板（用于复制到其余11篇）

- 样板文献：PEA009（10.1016/j.eswa.2024.124167）
- 本地全文：Artificial intelligence in education_ A systematic literature review - ScienceDirect.html
- 已提取锚点：
  - RQ：`#s0005/#p0025`
  - 方法与规模：`#p0045/#p0050/#p0225`
  - 应用分布：`#p0240`
  - 主题分布：`#p0325`
  - 方法分布：`#p0350`
  - 理论使用：`#p0385`
  - 教育阶段：`#p0390`

## 下一步执行顺序

1. 优先补 R2EA023、R2EA020、R2NA033、R2NA035（综述/元分析，参数复用价值高）。
2. 再补 R2NE038、R2NE015（直接关联教育落地场景）。
3. 最后补框架/概念型文献，并在边界字段中明确“不可当作效应证据”。

## 本轮更新结论（2026-04-11）

- 12 篇重点文献中，已落地可用来源 12 篇（11 HTML + 1 PDF-only）。
- R2EA007 由用户确认其本地来源文件：Artificial intelligence in education_ A systematic literature review - ScienceDirect.html。
- 下一步将按“已落地待抽锚”队列批量补齐 4 类字段（方法/样本/指标/边界）。
