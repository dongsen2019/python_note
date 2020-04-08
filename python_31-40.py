# lesson 31
# 变量的作用域
"""
局部变量：
    函数内定义的变量，作用域为块作用域，函数外不能使用
    在函数外定义的变量，函数可以访问，但是不能更改（以静态全局变量方式存在）
变量分两种：
    可变数据类型： 在函数外定义的变量， 在函数内可以操作和变更(列表和字典)
    不可变数据类型： 在函数外定义的变量，在函数内只能访问，不能使用其他操作
global
    在函数内部使用global可以引用函数外的变量和定义全局变量，可以操作和变更

globals() 获取全局数据
locals() 获取当前作用域的数据
"""

n = 10

def f():
    global n
    n = 11
    print(n)
    global i
    i = 12
    j = 3
    print(locals())

f() # *重点
print(i)
i += 1
print(i)

print(globals())

# lesson 32
# 关键字 nonlocal
"""
在嵌套函数的内层中如果想使用外层函数的变量，那么需要使用 nonlocal 关键字的引用

"""


def outer():
    """
    函数的说明文档
    :return: 无返回
    """
    num = 10

    def inner():
        nonlocal num
        # num = 1 不能用nonlocal关键字定义
        num += 1
        print(num)
    inner()


outer()
print(outer.__doc__) # 函数的说明文档调用
"""
__name__ ==> 当前脚本如果作为主程序，那么值是__main__，如果是当做一个模块，在另外一个脚本中引用去使用，则__name__的值是当前文件的名字
__doc__  ==> 当前脚本的文档说明 在当前脚本当中的第一个 三引号注释 就是当前脚本的说明文档

{
    '__name__': '__main__',
    '__doc__': '\n局部变量：\n    函数内定义的变量，作用域为块作用域，函数外不能使用'
    '__package__': None, 
    '__loader__': <_frozen_importlib_external.SourceFileLoader object at 0x0000000000191CC0>, 
    '__spec__': None, 
    '__annotations__': {}, 
    '__builtins__': <module 
    'builtins' (built-in)>, 
    '__file__': 'E:/pycharm/pythonspace/python_31-40.py', 
    '__cached__': None, 
    'n': 11, 'f': <function f at 0x00000000003EC1E0>, 'i': 13
}
"""