#!/usr/bin/env python3
"""
下载维吾尔语TTS模型
"""

from transformers import VitsTokenizer, VitsModel
import os

MODEL_PATH = "./model"
os.makedirs(MODEL_PATH, exist_ok=True)

print("正在下载模型...")
print("模型: facebook/mms-tts-uig-script_arabic")
print("大小: 约 145MB")
print()

# 下载并保存到本地
tokenizer = VitsTokenizer.from_pretrained("facebook/mms-tts-uig-script_arabic")
model = VitsModel.from_pretrained("facebook/mms-tts-uig-script_arabic")

# 保存到本地
tokenizer.save_pretrained(MODEL_PATH)
model.save_pretrained(MODEL_PATH)

print(f"\n模型已保存到: {MODEL_PATH}")
print("下载完成！")
