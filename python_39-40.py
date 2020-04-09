# lesson 39
# 匿名函数 lambda 表达式


"""
匿名函数不使用def定义，并且这个函数也没又名字
在python中可以使用lambda表达式来定义匿名函数
注意：lambda表达式仅仅是一个表达式，不是一个代码块，所以lambda又称为一行代码的函数
lambda表达式也用形参，并且不能访问除了自己的形参之外的任何数据包括全局变量
"""

res = lambda x, y: x + y
print(res(4, 4))

"""
lambda是一个表达式，不能写太复杂的逻辑，功能相对单一
"""

# lesson 40
# 迭代器是python中最具特色的功能之一，是访问集合元素的一种方式
# 迭代器是一个可以记住访问的位置的对象
# 从集合的第一个元素开始访问，直到集合中的所有元素被访问完毕
# 迭代器只能从前往后一个一个的遍历，不能后退
# 能被next()函数调用，并不断返回下一个值的对象称为迭代器(Iterator 迭代器对象)

"""
iter()
    功能：把可迭代的对象，转化为一个迭代器对象
    参数：可迭代的对象（str，list，tuple，dict，set，range...）
    返回值：迭代器对象
    能被next()函数调用，并不断返回下一个值的对象称为迭代器(Iterator 迭代器对象)
"""
arr = [1,2,3,4]
res = iter(arr) #iter()返回容器的begin()
print(next(res))
print(next(res))
print(next(res))
print(next(res))
# print(next(res))  #迭代器超尾 StopIteration

r = list(res)
print(r)


"""
迭代器的取值方案
1.next() 调用一次获取一次，直到数据被取完
2.list() 使用list函数直接取出迭代器中的所有数据
3.for    使用for循环遍历迭代器的数据
"""

#检测迭代器和可迭代对象的方法


from _collections_abc import Iterator,Iterable

varstr = "123456"
res = iter(varstr)

# type() 函数返回当前数据的类型
# isinstance() 检测一个数据是不是一个指定的类型
r1 = isinstance(varstr,Iterable)
r2 = isinstance(varstr,Iterator)
print(r1,r2)

r1 = isinstance(res,Iterable)
r2 = isinstance(res,Iterator)
print(r1,r2)







