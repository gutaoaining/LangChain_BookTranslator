# 作者：顾涛
# 创建时间：2025/5/10

class PageOutOfRangeException(Exception):
    def __init__(self, book_total_pages, translator_pages):
        self.book_total_pages = book_total_pages
        self.translator_pages = translator_pages
        super().__init__(f'页数的范围越界：这本书的总页数为：{book_total_pages},但是您输入的页数为：{translator_pages}')
