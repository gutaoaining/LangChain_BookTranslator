# 作者：顾涛
# 创建时间：2026/1/12
from ai_model.model import Model
from model.content import Content


class TranslatorChain:
    """
    负责调用langchain来完成文本的翻译
    """

    _instance = None

    def __init__(self, model: Model):
        self.langchain = model.make_prompt() | model.create_llm()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(TranslatorChain, cls).__new__(cls)
        return cls._instance

    def run(self, content: Content, source_language: str, target_language: str = '中文'):
        """
        翻译具体的文本，返回翻译之后的文本内容和翻译的状态
        :param content:
        :param source_language:
        :param target_language:
        :return: translation_text, status
        """
        pass
