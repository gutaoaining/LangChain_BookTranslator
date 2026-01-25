# 作者：顾涛
# 创建时间：2026/1/24
# import os
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# class GeminiTranslator:
#     def __init__(self, api_key: str):
#         self.client = genai.Client(
#             api_key=api_key,
#             http_options={"api_version": "v1"}  # ✅ v1
#         )
#
#         self.model_name = "models/gemini-1.5-flash"  # ✅ v1 可用模型
#
#         self.config = types.GenerateContentConfig(
#             temperature=0.1
#         )
#
#         self.system_prompt = (
#             "You are a professional translator. "
#             "Translate the user's input into Simplified Chinese accurately. "
#             "Maintain the original tone. Only output the translated text."
#         )
#
#     def translate(self, text: str) -> str:
#         try:
#             contents = [
#                 types.Content(
#                     role="system",
#                     parts=[types.Part(text=self.system_prompt)]
#                 ),
#                 types.Content(
#                     role="user",
#                     parts=[types.Part(text=text)]
#                 )
#             ]
#
#             response = self.client.models.generate_content(
#                 model=self.model_name,
#                 contents=contents,
#                 config=self.config
#             )
#
#             return response.text
#         except Exception as e:
#             return f"Translation Error: {e}"
#
#
# if __name__ == "__main__":
#     KEY = os.getenv("GEMINI_API_KEY")
#     translator = GeminiTranslator(api_key=KEY)
#
#     text = "The `google.genai` library is the new standard for accessing Gemini models."
#     print("译文:", translator.translate(text))
# from google import genai
#
# # The client gets the API key from the environment variable `GEMINI_API_KEY`.
# client = genai.Client()
#
# response = client.models.generate_content(
#     model="gemini-3-flash-preview", contents="中国的首都是哪个城市"
# )
# print(response.text)
#
# import os
# from google import genai
# from google.genai import types
# from dotenv import load_dotenv
#
# load_dotenv()
#
#
# def translate_en_to_zh(text: str) -> str:
#     client = genai.Client(
#         api_key=os.getenv("GEMINI_API_KEY"),
#         http_options={"api_version": "v1"}
#     )
#
#     contents = [
#         types.Content(
#             role="system",
#             parts=[types.Part(
#                 text=(
#                     "You are a professional translator. "
#                     "Translate the user's input into Simplified Chinese accurately. "
#                     "Maintain the original tone. Only output the translated text."
#                 )
#             )]
#         ),
#         types.Content(
#             role="user",
#             parts=[types.Part(text=text)]
#         )
#     ]
#
#     response = client.models.generate_content(
#         model="models/gemini-1.5-flash",
#         contents=contents,
#         config=types.GenerateContentConfig(
#             temperature=0.1
#         )
#     )
#
#     return response.text
#
#
# if __name__ == "__main__":
#     english = "The google.genai library is the new standard for accessing Gemini models."
#     chinese = translate_en_to_zh(english)
#     print("原文:", english)
#     print("译文:", chinese)
#
# from google import genai
# from google.genai import types
# import os
#
# client = genai.Client(
#     api_key=os.getenv("GEMINI_API_KEY"),
#     http_options={"api_version": "v1"}
# )
#
# def can_generate(model_name: str) -> bool:
#     try:
#         client.models.generate_content(
#             model=model_name,
#             contents="ping",
#             config=types.GenerateContentConfig(max_output_tokens=1)
#         )
#         return True
#     except Exception as e:
#         return False
#
# for m in client.models.list():
#     name = m.name
#     ok = can_generate(name)
#     print(name, "✅ generateContent" if ok else "❌ not supported")


import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def translate_en_to_zh(text: str) -> str:
    response = client.models.generate_content(
        model="models/gemini-2.5-flash",  # ✅ 你账号可用
        contents=[
            types.Content(
                role="user",
                parts=[types.Part(
                    text=(
                        "Translate the following English text into Simplified Chinese. "
                        "Keep the original tone. Only output the translation.\n\n"
                        f"{text}"
                    )
                )]
            )
        ],
        config=types.GenerateContentConfig(
            temperature=0.1
        )
    )
    return response.text


if __name__ == "__main__":
    english = "The google.genai library is the new standard for accessing Gemini models."
    print("译文:", translate_en_to_zh(english))