# lesson 137 导入方式的分类

"""
# 绝对导入
# 绝对导入的方式会使用[搜索路径]去查找和导入指定的包或模块
import 模块
import 包
import 包.模块
from 模块 import 类型
from 包 import 模块
from 包.模块 import 类型

#相对导入 注意：相对导入只能在非主程序的模块中使用，不需要直接运行的模块文件
from .包名/模块名 import 模块/内容
from ..包名/模块名 import 模块/内容

.代表当前
..代表上一级
"""

# 导入c模块。c模块中使用了相对导入（见package包中的c.py）
from package.ps import c

#了解 搜索路径
# 在导入模块或包时，程序查找的路径

"""
主要的搜索路径
1.当前导入模块的程序所在的文件
2.python的安装目录中 C:/Users/username/.../python37/lib
3.python解释器指定的其它 第三方模块位置 /lib/sitepackages
"""

# 在当前脚本中查看 包或模块 的 搜索路径
import sys
print(sys.path)
