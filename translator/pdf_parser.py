# 作者：顾涛
# 创建时间：2025/4/13
from typing import Optional

import pdfplumber

from model.Page import Page
from utils.log_utils import log
from exception.exception import PageOutOfRangeException
from model.book import Book
from model.content import Content, ContentType, TableContent


def parse_pdf(pdf_file_path: str, pages: Optional[int] = None) -> Book:
    '''
    解析pdf文件的函数，返回解析之后的文本对象
    :param pdf_file_path: pdf文件路径
    :param pages: 可选地，需要翻译前n页，默认是整个pdf
    :return: 返回一个Book对象
    '''
    book = Book(pdf_file_path)  # 一个pdf对应一本书，就是一个book对象
    with pdfplumber.open(pdf_file_path) as pdf:
        # pages不能超过pdf本身的页数
        if pages and pages > len(pdf.pages):  # 页数超过范围
            raise PageOutOfRangeException(len(pdf.pages), pages)
        if pages is None:  # 如果页数没有传值，则翻译整本书
            pages_arr = pdf.pages
        else:  # 如果传值了，则通过传入页做截取，截取前pages页数
            pages_arr = pdf.pages[:pages]

        for pdf_page in pages_arr:  # 遍历pdf的每一页
            page = Page()  # 每一页都是一个Page对象
            # 从pdf的page中截取文本内容
            row_text = pdf_page.extract_text()
            tables = pdf_page.extract_tables()
            # 出现重复的问题提取

            # 从raw_text中删除，表格中已经存在的文本
            for table in tables:
                for row in table:
                    for cell in row:
                        row_text = row_text.replace(cell, '', 1)
            # 处理文本内容
            if row_text:
                # 数据清晰：删除空行，和首尾空白字符
                lines = row_text.splitlines()
                cleaned_line = [line.strip() for line in lines if line.strip()]
                cleaned_text = '\n'.join(cleaned_line)

                # 文本内容对应一个Content对象
                text_content = Content(content_type=ContentType.TEXT, original=cleaned_text)
                page.add_content(text_content)  # 把内容添加的哦啊page中
                log.debug(f'[pdf解析之后的文本内容]：\n {cleaned_text}')
            # 处理所有表格
            if tables:
                tables_content = TableContent(content_type=ContentType.TABLE, original=tables)
                page.add_content(tables_content)  # 把表格内容添加到 page中去
                log.debug(f'[pdf解析之后的表格内容：]\n{tables_content}')
            book.add_page(page)  # 把每一个page对象添加到book中
    return book

# python-docx
