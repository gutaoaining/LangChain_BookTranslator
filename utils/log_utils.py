# 作者：顾涛
# 创建时间：2025/4/13
import sys, os
from loguru import logger

# 获取当前项目的绝对路径
root_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 存放在项目日志目录的路径
log_dir = os.path.join(root_path, 'logs')

# 如果日志目录地址不存在则创建
if not os.path.exists(log_dir):
    os.mkdir(log_dir)

# 存储日志的文件名
LOG_FILE_NAME = "translation.log"


# Trace < Debug < Info < Success < Warning < Error < Critical

class MyLogger:

    def __init__(self):
        log_file_path = os.path.join(log_dir, LOG_FILE_NAME)
        # 写日志的对象
        self.logger = logger
        # 清空所用设置
        self.logger.remove()
        # 添加控制台输出的格式，sys.stdout为输出到屏幕；关于这些配置还需要自定义请查看官网的相关参数说明
        self.logger.add(sys.stdout, level="INFO", format="<green>{time:YYYYMMDD HH:mm:ss}</green> | "  # 时间展示成绿色
                                                         "{process.name} | "  # 进程名
                                                         "{thread.name} | "  # 线程名
                                                         "<cyan>{module}</cyan>.<cyan>{function}</cyan>"  # 模块名.方法名
                                                         ":<cyan>{line}</cyan> | "  # 行号
                                                         "<level>{level}</level>: "  # 等级
                                                         "<level>{message}</level>"  # 日志内容
                        )
        # 输出到文件的格式
        self.logger.add(log_file_path, level='DEBUG', format='{time:YYYYMMDD HH:mm:ss} - '
                                                             "{process.name} | "
                                                             '{thread.name} | '
                                                             "{module}.{function}:{line} - {level} - {message}",
                        rotation="10 MB",  # 日志文件生成的规则 rotation=”1 week“ rotation=”1 days“
                        retention=50  # 保留日志的规则
                        )

    def get_logger(self):
        return self.logger


log = MyLogger().get_logger()
# if __name__ == '__main__':
#     log = MyLogger().get_logger()
#     log.debug("this is a debug message")
#     log.info("this is a info message")
#     log.warning("this is a warning message")
#     log.trace("this is a trace message")
#
#
#     @log.catch
#     def test():
#         try:
#             print(3 / 0)
#         except ZeroDivisionError as e:
#             log.error(e)
#             log.exception(e)
#
#
#     test()
