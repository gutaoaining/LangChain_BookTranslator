# 作者：顾涛
# 创建时间：2026/1/25
from ai_model.model import Model
from langchain_google_genai import ChatGoogleGenerativeAI


class GeminiAIModel(Model):

    def __init__(self, model_name: str, api_key: str):
        self.model_name = model_name
        self.api_key = api_key

    def create_llm(self):
        """
        初始化openai的大语言模型对象
        :return:
        """
        return ChatGoogleGenerativeAI(model=self.model_name, api_key=self.api_key, temperature=0)
