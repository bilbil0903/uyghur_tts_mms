#!/usr/bin/env python3
"""
MMS 维吾尔语语音合成 (TTS) - 离线版
模型路径: ./model/
"""

import torch
import numpy as np
from scipy.io import wavfile
from scipy.signal import butter, filtfilt
from transformers import VitsTokenizer, VitsModel

# 配置
MODEL_PATH = "./model"
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"
SAMPLE_RATE = 16000


def enhance_audio(waveform):
    """音频增强: 去噪 + 归一化"""
    # 低通滤波去噪
    nyquist = 0.5 * SAMPLE_RATE
    b, a = butter(5, 7500 / nyquist, btype='low')
    waveform = filtfilt(b, a, waveform)

    # 归一化
    waveform = waveform * (0.99 / np.max(np.abs(waveform)))

    return waveform


def tts(text, output_file):
    """文字转语音"""
    # 加载模型 (首次会加载, 之后用缓存)
    if not hasattr(tts, "model"):
        print("加载模型中...")
        tts.tokenizer = VitsTokenizer.from_pretrained(MODEL_PATH, local_files_only=True)
        tts.model = VitsModel.from_pretrained(MODEL_PATH, local_files_only=True).to(DEVICE)
        tts.model.eval()
        print("模型加载完成!")

    # 推理
    inputs = tts.tokenizer(text=text, return_tensors="pt")
    inputs = {k: v.to(DEVICE) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = tts.model(**inputs)

    # 处理音频
    waveform = outputs.waveform[0].cpu().numpy()
    waveform = enhance_audio(waveform)

    # 保存
    wavfile.write(output_file, SAMPLE_RATE, (waveform * 32767).astype(np.int16))
    print(f"已保存: {output_file}")


if __name__ == "__main__":
    # 测试
    texts = [
        ("ياخشىمۇسەن", "uyghur_tts_1.wav"),
        ("قانداق ئەھۋالىڭىز", "uyghur_tts_2.wav"),
    ]

    print(f"使用设备: {DEVICE}\n")
    for text, filename in texts:
        print(f"合成: {text}")
        tts(text, filename)
