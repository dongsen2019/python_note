# lesson 136 模块与包-自定义包和使用

"""
包:
    包可以理解为是一个文件夹，里面包含了多个python文件
包(文件夹)
|------ __init__.py  # 包的标志性文件(可以有内容，也可以没有)
|------a.py  # a模块(文件)
|------...等等文件
|------子包(文件夹中的文件夹)
|------|------__init__.py
|------|------c.py
|------|------d.py
"""

# 如果需要使用包可以直接导入包
# import package    # 只能导入__init__.py文件中的所有内容
# package.a.funca()  # AttributeError: module 'package' has no attribute 'a'

# 可以导入模块中的所有内容：注意这个内容是由 __init__.py文件中定义的 __all__ 这个变量指定的
# 注意格式 __all__ = ['a', 'b'],此时将不再导入__init__.py中的其它内容
from package import *
a.funca()
b.funcb()

# 导入指定包中的指定模块
from package import a
a.funca()

# 从指定包的指定模块中导入指定的内容
from package.b import funcb
funcb()

# 从指定包的子包中导入模块
from package.ps import c
c.funcc()

# 从指定包的子包的指定模块中导入指定数据
from package.ps.d import funcd
funcd()



