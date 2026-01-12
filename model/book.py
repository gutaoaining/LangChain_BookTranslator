# 作者：顾涛
# 创建时间：2025/4/13
from model.Page import Page


class Book:
    '''
    代表你需要翻译的一本书
    '''

    def __init__(self, file_path):
        self.file_path = file_path
        self.pages = []  # 这本所有的内容页

    def add_page(self, page: Page):
        self.pages.append(page)
