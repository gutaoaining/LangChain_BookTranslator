# 作者：顾涛
# 创建时间：2026/1/9
from ai_model.openai_model import OpenAIModel
from utils.project_config import ProjectConfig

if __name__ == '__main__':
    # 项目整体配置的初始化
    config = ProjectConfig()
    config.initialize()

    # 初始化大语言模型
    if config.model_type == 'OpenAIModel':
        model = OpenAIModel(config.model_name, config.api_key)
    else:
        pass