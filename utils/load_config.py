# 作者：顾涛
# 创建时间：2025/3/26
import yaml


class LoaderConfig:
    def __init__(self, file_config_path):
        self.config_path = file_config_path

    def load_config(self):
        '''
        加载配置文件
        :return:
        '''
        with open(self.config_path, 'r') as f:
            config = yaml.safe_load(f)

        return config
