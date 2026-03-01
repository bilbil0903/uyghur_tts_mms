# Uyghur TTS MMS

维吾尔语语音合成工具，基于 Meta MMS 模型。

## 特点

- 完全离线运行，无需联网
- 支持维吾尔语（阿拉伯字母）文字转语音
- 音质优化（降噪、归一化）
- 轻量级，模型仅 145MB

## 模型信息

- **模型**: facebook/mms-tts-uig-script_arabic
- **大小**: 145MB
- **采样率**: 16kHz

## 使用方法

### 1. 下载模型

```bash
python3 download_model.py
```

### 2. 运行TTS

```bash
python3 tts_uyghur.py
```

## 自定义文本

编辑 `tts_uyghur.py` 文件中的 `texts` 列表：

```python
texts = [
    ("ياخشىمۇسەن", "output_1.wav"),
    ("مەن سىزنى سۆيىمەن", "output_2.wav"),
]
```

## 依赖

```bash
pip install torch transformers scipy
```

## 文件结构

```
.
├── tts_uyghur.py       # 主脚本
├── download_model.py   # 模型下载脚本
├── model/              # 离线模型文件 (运行下载脚本后生成)
└── README.md
```
