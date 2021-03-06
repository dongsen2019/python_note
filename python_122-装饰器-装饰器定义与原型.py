# lesson 122 装饰器定义与原型


"""
# 装饰器   decorator

1.在不改变原有函数代码，且保持原函数调用方法不变的情况下，给原函数增加新的功能(或者给类增加属性和方法)
2.核心思想：用一个函数（或者类）去装饰一个旧函数（或者类），造出一个新韩淑（或者新类）
3.语法规则：在原有的函数上加上 @符，装饰器会把下面的函数当作参数传递到装饰器中，@符 又被称为 语法糖
4.应用场景：引入日志，函数执行时间的统计，执行函数前的准备工作，执行函数后的处理工作，权限校验，缓存等场景中

@outer
def func():
    pass
"""

# 1.装饰器的原型

### 装饰器的本质就是利用闭包函数，把函数当作参数传递，并且在函数内去调用传递进来的函数，并且返回一个函数

# 定义外函数，接收一个函数作为参数
def outer(f):
    # 定义内函数，并且在内函数中调用了外函数的参数
    def inner():
        print("我是外函数中的内函数1")
        f()
        print("我是外函数中的内函数2")
    return inner

# 定义普通函数
def old():
    print("普通函数")

"""
# old()     # 作为普通函数直接调用
old = outer(old)      # outer 返回了inner函数，赋值给了old
old()                   # 此时再调用old函数时，等同于调用了 inner 函数
"""


# 改为装饰器用法
@outer
def old():
    print("普通函数")

old()  #old函数经过 outer 装饰器进行了装饰，代码和调用方法不变，但是函数的功能触发了改变






