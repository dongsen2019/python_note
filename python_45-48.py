# lesson 45
# 内置函数-高阶函数 sorted()
"""
运行原理：
    把可迭代数据里面的元素，通过用户给定的函数进行处理并按照返回结果排序
    返回一个新的列表
功能：排序
参数：
    iterable 可迭代的数据(容器类数据，range数据序列，迭代器)
    reverse  可选参数，是否反转，默认值为False，不反转，True为反转
    key      可选参数，函数，可以是自定义函数(包括lambda)，也可以是内置函数
返回值： 排序后的结果
"""

arr = [3,7,1,-9,20,10]
res1 = sorted(arr)
res2 = sorted(arr, reverse=True)
res3 = sorted(arr, key=abs)
print(res1)
print(res2)
print(res3)


# lesson 46
# 内置函数-高阶函数 map()
# 对传入的可迭代数据中的每个元素进行处理，返回一个新的迭代器
"""
map(func, *iterables)
参数：
    func 函数，自定义函数|内置函数
    iterables： 可迭代的对象
返回值：迭代器
"""

varlist = ['1', '2', '3', '4']
res = map(lambda x: int(x), varlist)
print(list(res))

varlist = [1, 2, 3, 4]
res = map(lambda x: pow(x, 2), varlist)
print(list(res))

varlist = ['a', 'b', 'c', 'd']
res = map(lambda x: ord(x.upper()), varlist)
print(list(res))

# lesson 47
# 内置函数-高阶函数 reduce()

# reduce() 的使用先要导入

from functools import  reduce


"""
reduce(func,iterable)
功能：
    首次取出迭代对象的前两个元素进行处理，之后每次都将返回的结果和下一个元素继续运算处理
    知道元素耗尽为止
参数：
    func： 内置函数或者自定义函数
    iterable：可迭代对象
返回值：最终的运算处理结果
注意： 使用 reduce() 的时候先要导入
"""


varlist = [5, 2, 1, 1]

res = reduce(lambda x, y: str(x)+str(y), varlist)
print(int(res))

s1 = "456"

res = reduce(lambda x, y: 10*int(x)+int(y), s1)
print(res)


# lesson 48
# filter() 过滤器

"""
filter(func, iterable)
功能： 过滤数据，把 iterable 中的每个元素用func判断，
       如果函数返回True则保留，False则丢弃
参数：
        func： 自定义函数
        iterable： 可迭代对象
返回值： 保留下来的数据组成的迭代器
"""

# 保留所有的偶数，丢弃所有的奇数
varlist = [1,2,3,4,5,6,7,8,9,0]


def toe(x):
    if x % 2 == 0:
        return True
    else:
        return False


res = filter(toe, varlist)
print(list(res))