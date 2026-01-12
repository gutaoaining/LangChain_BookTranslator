# 作者：顾涛
# 创建时间：2025/5/10
from typing import Optional

from ai_model.model import Model
from translator.file_writer import FileWriter
from translator.pdf_parser import parse_pdf
from translator.translator_chain import TranslatorChain
from utils.log_utils import log


class PDFTranslator:
    '''
     翻译一个pdf文件的书籍
    '''

    def __init__(self, model: Model):
        self.book = None
        self.chain = TranslatorChain(model)  # 负责翻译文本的
        self.writer = FileWriter(self.book)

    def translate_book(self, file_path: str, source_language: str, target_language: str = '中文',
                       out_file_format: str = 'PDF',
                       out_file_path: str = None, pages: Optional[int] = None):
        """
        翻译一本书
        :param file_path: 输的文件路径
        :param source_language: 源语言
        :param target_language: 目标的语言
        :param out_file_format: 输出的文件格式
        :param out_file_path: 输出文件路径
        :param pages: 翻译的页
        :return:
        """
        self.book = parse_pdf(file_path, pages)  # 解析文件得到一个book对象

        self.writer.book = self.book
        for page_index, page in enumerate(self.book.pages):  # 遍历所有的页
            for content_index, content in enumerate(page.contents):
                # 开始翻译每一个内容
                # 1、得到翻译的提示文本

                translation_text, status = self.chain.run(content, source_language, target_language)

                log.debug(f'翻译之后的文本：\n {translation_text}')
                # 把翻译之后的文本和状态设置到content对象中保存
                self.book.pages[page_index].contents[content_index].sst_translation(translation_text, status)
        # 把翻译之后的所有数据，写入文件
        # Writer
        self.writer.save_book(out_file_path, out_file_format)
