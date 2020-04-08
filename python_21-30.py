# lesson 27
# 函数的收集参数
# 收集参数负责收集多余的实参
# 或者说当不确定有多少个实参要传入时，可以使用一个收集参数来接受
# 在定义函数时，如果需要收集参数，那么这个形参前面需要加一个 * 号 例如 *args
# 接收的多余的参数，会存储在args中，形成一个元祖


def func(a, b, x='+', *args):
    print(type(args))
    if x == '+':
        print('加法运算', args)
    else:
        print('减法运算', args)


func(1, 2, '-', 200, 300, 400)

# 输出:
# <class 'tuple'>
# 减法运算 (200, 300, 400)


# lesson 28
# 命名关键字参数
'''
1.关键字参数定义在 收集参数 后面
2.关键字参数必须通过形参的名字来进行传递
3.一般地，普通函数的普通参数按照关键字参数进行传递，从而可以改变传递普通参数的顺序
'''


def love(a, b, c=3, *args, name="admin"):
    print(a, b, c)
    print(args)
    print(name)


love(1, 2, 3, 4, 5, 6, 7, 8, 9, name="dongsen")

# 输出:
# 1 2 3
# (4, 5, 6, 7, 8, 9)
# dongsen


# lesson 29
# 关键字参数收集
def love(a, b, c=3, *args, name, age, **kwargs):
    print(a, b, c)
    print(args)  # 普通收集参数,会把多余的参数收集成为元祖
    print(kwargs)  # 关键字参数收集，会把多余的关键字参数收集为 字典


love(1, 2, 3, 4, 5, name="dong", age="sen", aa='1', bb='2', cc='3')

# 输出:
# 1 2 3
# (4, 5)
# {'aa': '1', 'bb': '2', 'cc': '3'}


