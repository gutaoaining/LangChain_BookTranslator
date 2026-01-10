# 作者：顾涛
# 创建时间：2026/1/10
from ai_model.model import Model


class OpenAIModel(Model):

    def create_llm(self):
        """
        初始化openai的大语言模型对象
        :return:
        """
