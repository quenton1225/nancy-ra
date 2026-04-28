# Eye Tracking MVP Demo Design

**日期**: 2026-04-28  
**对应 source pack**: `67_eye_tracking_source_pack_20260428.md`  
**实现目录**: `eye_tracking_demo/`

## 1. 设计目标

本 demo 验证普通笔记本摄像头 + WebGazer 能否形成阅读任务的最小数据闭环：

1. 浏览器端摄像头 gaze 估计。
2. 9 点校准。
3. 3 段阅读材料。
4. 每段后 TUT / difficulty / familiarity probe。
5. 3 道理解题。
6. 本地导出 CSV。
7. Python 标准库脚本提取 paragraph-level 特征。

## 2. 安全边界

- 不保存视频。
- 不做人脸识别。
- 不做诊断分类。
- 只保存 gaze 坐标、任务事件、probe 与理解题结果。
- 数据默认留在本机。

## 3. 当前文件

| 文件 | 作用 |
| --- | --- |
| `eye_tracking_demo/index.html` | 浏览器任务页面 |
| `eye_tracking_demo/styles.css` | 简洁研究任务界面 |
| `eye_tracking_demo/app.js` | WebGazer 启动、校准、任务流、CSV 导出 |
| `eye_tracking_demo/README.md` | 运行说明和隐私边界 |
| `eye_tracking_demo/analysis/extract_features.py` | raw CSV 到 trial-level features |
| `eye_tracking_demo/vendor/webgazer-3.5.3.js` | 固定版本 WebGazer bundle |
| `eye_tracking_demo/mediapipe/face_mesh/` | WebGazer 所需 FaceMesh 本地运行时资源 |

## 4. 与 C007 的对应关系

| C007 原文 | MVP 对应 |
| --- | --- |
| WebGazer browser-based tracking | 使用 WebGazer CDN |
| Reading paragraphs | 3 段短文本 |
| 7 thought probes | 每段后 1 个 TUT probe，共 3 次 |
| 10 comprehension questions | 3 道理解题 |
| gaze/text/interaction features | valid ratio, offscreen ratio, dispersion, reading duration |
| 不用于诊断 | MVP 明确不输出身份标签 |

## 5. 运行方式

从仓库根目录运行：

```powershell
c:/Users/Quenton/Documents/Github/nancy-ra/.venv/Scripts/python.exe -m http.server 8765 -d eye_tracking_demo
```

然后打开：

```text
http://localhost:8765
```

## 6. 下一步验证

1. 在 Chrome/Edge 中打开本地地址。
2. 允许摄像头权限。
3. 完成一次校准、阅读、probe、理解题。
4. 导出 CSV。
5. 运行 `analysis/extract_features.py`。
6. 记录是否出现 WebGazer 加载失败、摄像头权限失败、gaze 缺失或导出字段错误。
