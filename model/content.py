# 作者：顾涛
# 创建时间：2025/4/13
import re
from email.header import Header
from enum import Enum, auto

import pandas as pd
from utils.log_utils import log


class ContentType(Enum):
    '''
    内容的类型枚举
    '''
    TEXT = auto()
    TABLE = auto()
    IMAGE = auto()


class Content:
    '''书中的文本内容'''

    def __init__(self, content_type: ContentType, original, translation=None):
        '''
        内容的初始化
        :param type: 类型
        :param original: 原文
        :param translation: 翻译之后
        '''
        self.content_type = content_type
        self.original = original
        self.translation = translation
        self.status = False

    def sst_translation(self, translation, status):
        '''设置翻译后的文本，并设置翻译状态'''
        if self.content_type == ContentType.TEXT and isinstance(translation, str) and status:
            self.translation = translation
            self.status = status
        else:
            log.warning('当前翻译之后的文本内容，不是字符串，请检查')

    def check_translation_type(self, translation):
        pass

    def get_original_to_string(self):
        '''把DataFrame对象转换成字符串'''
        return self.original


class TableContent:
    '''书中的表格内容'''

    def __init__(self, content_type: ContentType, original, translation=None):
        '''
        内容的初始化
        :param type: 类型
        :param original: 原文
        :param translation: 翻译之后
        '''
        df = pd.DataFrame(original)
        self.content_type = content_type
        self.original = df
        self.translation = translation
        self.status = False

    @log.catch
    def sst_translation(self, translation, status):
        pass
        """
        设置翻译之后的文本，并设置翻译状态
        1、判断数据的合法性
        2、把translation文本数据，变成二维数组
        3、把二维数据变成DataFrame
        """
        if self.content_type == ContentType.TABLE and isinstance(translation, str) and status:
            # 得到二维数组
            table_data = [re.split(',|，', row.strip()) for row in translation.strip().split('\n')]
            log.debug(table_data)
            # 得到dataFrame数据，表头单独处理
            translation_df = pd.DataFrame(table_data[0:])
            log.debug(f"处理成DataFrame数据：\n{translation_df}")
            self.translation = translation_df
            self.status = status

    def get_original_to_string(self):
        '''把DataFrame对象转换成字符串'''
        return self.original.to_string(header=False, index=False)
