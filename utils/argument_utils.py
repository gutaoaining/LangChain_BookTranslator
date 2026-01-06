# 作者：顾涛
# 创建时间：2025/3/23
import argparse


class ArgumentUtils:
    def __init__(self):
        self.parser = argparse.ArgumentParser(description='书籍自动翻译器')
        self.parser.add_argument('--config', type=str, default='config.yaml', help='项目的整体配置文件')
        self.parser.add_argument('--model_type', type=str,  default='OpenAIModel',
                                 choices=['GLMModel', 'OpenAIModel'], help='选择OpenAI还是GLM的模型')
        self.parser.add_argument('--glm_model_url', type=str, help='ChatGLM的模型访问地址')

        self.parser.add_argument('--timeout', type=str, help='API接口请求超时时间')
        self.parser.add_argument('--openai_model', type=str, help='OPENAI中所使用的模型名字')
        self.parser.add_argument('--openai_api_key', type=str, help='OPENAI中的api_key')
        self.parser.add_argument('--book', type=str, help='需要翻译的书籍所属的文件路径')
        self.parser.add_argument('--file_format', type=str, help='翻译之后生成的文件格式')

    def parse_argument(self):
        '''
        解析和验证命令中的参数
        :return:
        '''
        arguments = self.parser.parse_args()
        # 参数验证
        # if arguments.model_type == 'OpenAIModel' and not arguments.openai_model and not arguments.openai_api_key:
        #     self.parser.error('选择OPENAI之后，--openai_model和--openai_api_key，参数为必传！')
        return arguments
