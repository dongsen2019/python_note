# lesson 135 python中的模块与包

"""
模块：
    定义的一个python的文件，后缀名为.py。这个文件被称为模块
    模块中通常会定义一些相似的类，函数等代码内容。提供给别的程序引入后使用。
系统模块：
    系统模块就是一个python的程序脚本，专门提供给我们自己的程序使用。他们是在安装好python环境时，就
    已经存在的，需要的时候可以使用import导入到程序中使用。

    import logging，json，time。。。
自定义模块：
    就是自己创建一个python脚本，定义一些类或方法，供别的脚本导入后使用。
"""

import My
print(My.__name__)


# 想使用模块中的内容时，除了导入模块，还可以在指定模块中导入指定的内容
from My import love # 导入My模块中的love变量
from My import love as lv # 导入My模块中的love变量，起个别名
print(love)
print(lv)
