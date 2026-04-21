# 剩余缺摘要条目检索日志（2026-04-11）

## 当前状态

- 54号证据库覆盖：40/40
- 已补回：R2NA042（LWW出版社全文可读段落）、R2NE019（KCL仓储PDF）、PNE004（UEA仓储PDF）、PEA010（Figshare开放稿PDF）、PEA009（本地保存ScienceDirect页面解析）
- 仍缺：0篇

## 仍缺条目

| record_id | doi | title |
|---|---|---|
（无）

## 已尝试来源与结果

1. Crossref Works API
- 结果：4/4 未返回 abstract 字段。

2. OpenAlex（works by DOI + filter查询）
- 结果：4/4 未返回可重建摘要；filter 查询为空。

3. Semantic Scholar Graph API
- 结果：3/4 返回无摘要，1/4 返回错误/不可用。

4. Europe PMC
- 结果：4/4 无摘要返回。

5. DOI 重定向落地页抓取（Elsevier LinkingHub）
- 结果：页面为脚本驱动壳层，未暴露摘要正文（仅PII与基础元信息）。

## 访问限制说明

- 其中3篇（R2NE019、PNE004、PEA010）通过开放仓储或Figshare开放稿PDF补回摘要。
- PEA009 通过本地保存的 ScienceDirect 页面中的预加载状态字段解析补回摘要。

## 下一步补齐策略

1. 摘要补齐已完成，下一步建议转向全文证据（段落+页码/节号）与方法复现卡。
2. 复核作者预印本/机构仓储是否存在同题版本可用摘要。
3. 若仍不可得，在组会材料中保持“4篇证据缺口”明示，避免口径夸大。
