# 作者：顾涛
# 创建时间：2025/4/13
from model.content import Content


class Page:
    '''
    代表书里面一页的内容
    '''

    def __init__(self):
        self.contents = []

    def add_content(self, content: Content):
        self.contents.append(content)
