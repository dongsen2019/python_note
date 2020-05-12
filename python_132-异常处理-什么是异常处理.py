# lesson 130 异常处理-什么是异常处理

"""
异常分两种：
    1.语法错误导致的异常
    2.逻辑错误导致的异常

例如：获取一个不存在的索引
"""
# varlist = [1, 2, 3]
# print(varlist[3])  # IndexError: list index out of range


# Python 异常错误类
"""
BaseException	所有异常的基类
SystemExit	解释器请求退出
KeyboardInterrupt	用户中断执行(通常是输入^C)
Exception	常规错误的基类
StopIteration	迭代器没有更多的值
GeneratorExit	生成器(generator)发生异常来通知退出
StandardError	所有的内建标准异常的基类
ArithmeticError	所有数值计算错误的基类
FloatingPointError	浮点计算错误
OverflowError	数值运算超出最大限制
ZeroDivisionError	除(或取模)零 (所有数据类型)
AssertionError	断言语句失败
AttributeError	对象没有这个属性
EOFError	没有内建输入,到达EOF 标记
EnvironmentError	操作系统错误的基类
IOError	输入/输出操作失败
OSError	操作系统错误
WindowsError	系统调用失败
ImportError	导入模块/对象失败
LookupError	无效数据查询的基类
IndexError	序列中没有此索引(index)
KeyError	映射中没有这个键
MemoryError	内存溢出错误(对于Python 解释器不是致命的)
NameError	未声明/初始化对象 (没有属性)
UnboundLocalError	访问未初始化的本地变量
ReferenceError	弱引用(Weak reference)试图访问已经垃圾回收了的对象
RuntimeError	一般的运行时错误
NotImplementedError	尚未实现的方法
SyntaxError	Python 语法错误
IndentationError	缩进错误
TabError	Tab 和空格混用
SystemError	一般的解释器系统错误
TypeError	对类型无效的操作
ValueError	传入无效的参数
UnicodeError	Unicode 相关的错误
UnicodeDecodeError	Unicode 解码时的错误
UnicodeEncodeError	Unicode 编码时错误
UnicodeTranslateError	Unicode 转换时错误
Warning	警告的基类
DeprecationWarning	关于被弃用的特征的警告
FutureWarning	关于构造将来语义会有改变的警告
OverflowWarning	旧的关于自动提升为长整型(long)的警告
PendingDeprecationWarning	关于特性将会被废弃的警告
RuntimeWarning	可疑的运行时行为(runtime behavior)的警告
SyntaxWarning	可疑的语法的警告
UserWarning	用户代码生成的警告
"""

# 1.如果错误发生的情况可以预知的，那么就可以使用流程控制进行预防处理
# 比如：两个数字的运算，其中一个不是数字，运算就会出错。这时可以去判断来预防

"""
n1,n2 = 2 '3'
res = n1 + n2
print(res)
"""

# 2.如果错误的发生条件不可预知，就可以使用 try...except... 在错误发生时进行处理
"""
语法：
    try：
        可能发生异常错误的代码
    except：
        如果发生异常则进入 except 代码块进行处理
"""

try:
    with open("./111.txt", 'r', encoding="utf-8") as fp:
        res = fp.read()
    print(res)
except:
    print("文件不存在")

print("程序继续执行。。。")




