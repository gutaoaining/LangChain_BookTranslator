# 作者：顾涛
# 创建时间：2026/1/6
import argparse


class ArgumentUtils:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='书籍自动翻译器')
        self.parser.add_argument('--config', type=str, default='config.yaml', help='项目的整体配置文件')
        self.parser.add_argument('--model_type', type=str, default='GeminiAIModel',
                                 choices=['GeminiAIModel', 'OpenAIModel'], help='选择OpenAI还是GLM的模型')
        self.parser.add_argument('--model_name', type=str, help='大语言模型名')
        self.parser.add_argument('--input_file', type=str, help='需要翻译的文件所属路径')
        self.parser.add_argument('--file_format', type=str, help='翻译之后生成的文件格式')
        self.parser.add_argument('--source_language', type=str, help='书籍的源语言')
        self.parser.add_argument('--target_language', type=str, help='翻译后的目标语言')

    def parse_argument(self):
        """
        解析和验证命令中的参数
        :return:
        """
        arguments = self.parser.parse_args()
        # 参数验证
        # if arguments.model_type == 'OpenAIModel' and not arguments.openai_model and not arguments.openai_api_key:
        #     self.parser.error('选择OPENAI之后，--openai_model和--openai_api_key，参数为必传！')
        return arguments
