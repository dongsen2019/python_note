# lesson 132 异常回溯和异常日志

# 自定义异常类日志处理类

class Myexception():
    def __init__(self):
        import traceback
        import logging


        logging.basicConfig(
            filename="./error.log",  # 日志存储的文件及目录
            format = "%(asctime)s %(levelname)s \n %(message)s",  # 格式化存储的日志格式
            datefmt = "%Y-%m-%d %H:%M:%S"
        )

        # 写入日志
        logging.error(traceback.format_exc())

# 使用自定义异常处理类
try:
    int("aa")
except:
    print("在此处进行异常处理")
    Myexception()   # 在异常处理的代码块中去调用自定义的异常处理类