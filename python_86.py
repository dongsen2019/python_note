# os.path   系统模块中的路径模块

import os

# 将相对路径转化为绝对路径  ***重要，使得代码可移植性增强
res = os.path.abspath("./")     # E:\pycharm\pythonspace

# 获取路径中的主体部分 就是返回路径中的最后一部分
res = os.path.basename("E:\pycharm\pythonspace")  # pythonspace

# 获取路径中的路径部分 返回路径中最后一部分之前的路径内容
res = os.path.dirname("E:\pycharm\pythonspace")  # E:\pycharm

# join()    连接多个路径，组成一个新的路径
res = os.path.join(".\\a\\b\c","ds.jpg")  # .\a\b\c\ds.jpg


# split() 拆分路径，把路径拆分为路径和主体部分
res = os.path.split(".\\abc\def\\aaa")  # ('.\\abc\\def', 'aaa')

# splitext() 拆分路径，可以拆分文件后缀名
res = os.path.splitext(".\\a\\b\c\ds.jpg")  # ('.\\a\\b\\c\\ds', '.jpg')

# 获取文件的大小 单位：字节
res = os.path.getsize("./test.py")  # 346B

# 检测是否是一个文件夹,是否存在
res = os.path.isdir("../pythonspace")  # True

# 检测文件是否存在
res = os.path.isfile("./test.py")  # True

# exists() 检测路径是否存在,既可以检测文件，也可以检测路径
res = os.path.exists("../pythonspace") # True
res = os.path.exists("../pythonspace/test.py") # True


# a和b是两个路径，比较两个path是否是同一个路径位置 （两个路径必须真实存在）
# res = os.path.samefile(a, b)
print(res)

