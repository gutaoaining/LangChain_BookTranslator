# 作者：顾涛
# 创建时间：2026/1/24
import os
import google.generativeai as genai
from dotenv import load_dotenv

# 加载 .env 文件中的 API_KEY
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") # 确保你的环境变量里有这个 key

# 1. 配置 API
genai.configure(api_key=api_key)

# 2. 初始化模型
# 使用 flash 模型，速度快，适合高频翻译任务
model = genai.GenerativeModel('gemini-1.5-flash')

# 3. 发送翻译请求
text_to_translate = "I am a Python developer looking to integrate AI."
prompt = f"Please translate the following English text to Chinese: \n{text_to_translate}"

try:
    response = model.generate_content(prompt)
    print(f"原文: {text_to_translate}")
    print(f"译文: {response.text}")
except Exception as e:
    print(f"Error: {e}")
