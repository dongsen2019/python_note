# lesson 61
# 元组

"""
元组定义
    1.定义元组 variable = () ，或者 variable = tuple
    2.还可以使用 variable = (1,2,3) 定义含有数的元组
    3.注意：如果元组中只有一个元素时，必须添加逗号 variable = (1,)
    4.特别地：variable = 1,2,3 这种方式也可以定义为一个元组
"""

# 元组的相关操作

"""
由于元组是不可变的数据类型，因此只能使用索引进行访问，不能进行其它操作
元组可以和列表一样使用切片方式获取元素
"""

# 单元素元组，需要添加逗号
vart = (1,)

# 获取元组的长度 len()
print(len(vart))

# 元组的切片操作 和列表一样

# 统计一个元素在元组中出现的次数
vart = (1, 2, 3, 4, 5, 6, 7, 5, 6, 7)
print(vart.count(5))

# 获取一个元素在元组的索引值
res = vart.index(5)
print(res)
res = vart.index(5, 5)
print(res)


# lesson 62
# 元组推导式，生成器

"""
列表推导式语法：
    [f(variable) for i in c] ==> 返回一个 列表
元组推导式
    (f(variable) for i in c) ==> 返回一个 生成器

生成器是什么？
    生成器是一个特殊的迭代器，生成器可以自定义，也可以使用元组推导式去定义
    生成器是按照某种算法去推算下一个数据或结果，只需要往内存中存储一个生成器，节约内存消耗，提升性能
语法：
    (1) 里面是推导式，外面是一个()的结果是一个生成器
    (2) 自定义生成器，含有yield关键字的函数就是生成器
        含有yield关键字的函数，返回的结果是一个迭代器，换句话说，生成器就是一个返回迭代器的函数

如何使用生成器？
    生成器是迭代器的一种，因此可以使用迭代器的操作方法来操作生成器
"""

# 列表推导式
varlist = [1,2,3,4,5,6,7,8,9]
newlist = [i**2 for i in varlist]
print(newlist)

#元组推导式

newt = (i**2 for i in varlist)

# 生成器可以使用next函数或者list、tuple函数进行操作
print(newt)
print(next(newt))
print(list(newt))
print(tuple(newt))

# 使用 for 循环进行遍历
newt = (i**2 for i in varlist)
for i in newt:
    print(i)

