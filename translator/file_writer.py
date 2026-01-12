# 作者：顾涛
# 创建时间：2025/6/1
import pandas as pd
from reportlab.lib import pagesizes, colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle, Table, PageBreak

from model.content import ContentType
from utils.log_utils import log


class FileWriter:
    def __init__(self, book):
        self.book = book

    def save_book(self, out_file_path, file_format):
        """
        负责把翻译之后的数据写入一个文件
        :param out_file_path:
        :param file_format:
        :return:
        """
        if file_format.lower() == 'pdf':
            self.save_book_pdf(out_file_path)
        elif file_format.lower() == 'md':
            self.save_book_markdown(out_file_path)
        elif file_format.lower() == 'doc' or file_format.lower() == 'docx':
            pass
        else:
            log.warning("当前的文件格式不支持：项目仅支持PDF、WORD、MarkDown这三种！å")
            return

    def save_book_pdf(self, out_file_path: str = None):
        """
        把数据写入PDD文件中
        :param out_file_path:
        :return:
        """
        if not out_file_path:
            subfix = self.book.file_path[self.book.file_path.rindex('.'):]
            out_file_path = self.book.file_path.replace(subfix, '_translated.pdf')
            # 写数据到文件中
            log.debug(f'pdf源文件路径：{self.book.file_path}，翻译后的文件路径：{out_file_path}')
            # 1、先注册中文字体
            pdfmetrics.registerFont(TTFont('SimSun', '../fonts/simsun.ttc'))

            # 2、创建一个pdf的文件段落样式
            style = ParagraphStyle('SimSun', fontName='SimSun', fontSize=12, leading=14)
            # 3、创建一个pdf的文档
            doc = SimpleDocTemplate(out_file_path, pagesize=pagesizes.letter)
            pdf_data = []  # 存放临时写入PDF文件的数据
            for page in self.book.pages:  # 循环这本书中所有的页
                for content in page.contents:
                    if content.status:
                        # 分两种情况，文字段落和表格
                        if content.content_type == ContentType.TEXT:
                            # 写一个段落
                            paragraph = Paragraph(text=content.translation, style=style)
                            pdf_data.append(paragraph)
                        elif content.content_type == ContentType.TABLE:
                            # 写入一个表格
                            table_style = TableStyle(  # 表格的样式，（0，0）代表第一行第一列，每组坐标为（列，行）
                                [
                                    ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
                                    ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
                                    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                                    ('FONTNAME', (0, 0), (-1, 0), 'SimSun'),  # 更改表头字体为 "SimSun"
                                    ('FONTSIZE', (0, 0), (-1, 0), 14),
                                    ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                                    ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
                                    ('FONTNAME', (0, 1), (-1, -1), 'SimSun'),  # 更改表格中的字体为 "SimSun"
                                    ('GRID', (0, 0), (-1, -1), 1, colors.black)
                                ]
                            )
                            # 把DataFrame转换成列表，并且创建一个表格对象
                            table = Table(data=content.translation.values.tolist(), colWidths=1.5 * inch,
                                          rowHeights=0.5 * inch)

                            table.setStyle(table_style)  # 设置样式
                            pdf_data.append(table)
                # 当前这一页的内容都处理了，紧跟着要加一页分页符
                # 分页符不能加在最后一页
                if page != self.book.pages[-1]:
                    pdf_data.append(PageBreak())  # 除了最后一页，每页的最后面都要加一个分页符

            doc.build(pdf_data)
            log.info('pdf文件写入完成！')

    def save_book_markdown(self, out_file_path: str = None):
        """
        把数据写入MarkDown文件中
        :param out_file_path:
        :return:
        """
        if not out_file_path:
            subfix = self.book.file_path[self.book.file_path.rindex('.'):]
            out_file_path = self.book.file_path.replace(subfix, '_translated.md')
            # 写数据到文件中
            log.debug(f'Markdown源文件路径：{self.book.file_path}，翻译后的文件路径：{out_file_path}')
            # 1、先注册中文字体
            with open(out_file_path, 'w', encoding='UTF-8') as md_file:
                for page in self.book.pages:  # 循环这本书中所有的页
                    for content in page.contents:
                        if content.status:
                            # 分两种情况，文字段落和表格
                            if content.content_type == ContentType.TEXT:
                                # 写一个段落
                                md_file.write(content.translation + '\n\n')
                            elif content.content_type == ContentType.TABLE:
                                # 写入一个表格
                                df: pd.DataFrame = content.translation  # 翻译之后的表格数据
                                first_row = df.values.tolist()[0]

                                df.columns = first_row

                                df.drop([0], inplace=True)
                                header = '| ' + ' | '.join(
                                    [str(column_name) for column_name in df.columns]) + ' |' + '\n'
                                tr = '| ' + ' | '.join(['---'] * len(df.columns)) + ' |' + '\n'
                                t_body = '\n'.join(['| ' + ' | '.join(str(cell) for cell in row) + ' |' for row in
                                                    df.values.tolist()]) + '\n\n'
                                md_file.write(header + tr + t_body)
                                # 当前这一页的内容都处理了，紧跟着要加一页分页符
                                # 分页符不能加在最后一页
                    if page != self.book.pages[-1]:
                        md_file.write('\n -----\n\n')  # 除了最后一页，每页的后面都加上一个分页符

            log.info('Markdown文件写入完成！')
