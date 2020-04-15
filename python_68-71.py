# lesson 68
# set 对象是由具有唯一性的 hashable 对象所组成的无序多项集。
# 因此类型为列表的元素不能添加到集合中 un-hashable

"""
集合定义的实现：
    1.可以直接用{}来定义集合
    2.可以使用set{}进行集合的定义和转换
    3.使用集合推导式完成集合的定义
    注意：集合中的元素不能重复，集合中存放的数据
"""

# 集合是无序的
# 集合中False和0只能存在一个,True和1只能存在一个
# 元素的唯一性
vars = {0,1,2,3,'abc','love',True,(1,2,3),0,False,3.1415,123}
print(vars)

# 检测集合中的值
res = '123' in vars
res = '123' not in vars

# 获取集合中的元素的个数 len()
res = len(vars)
print(res)

# 集合的遍历
for i in vars:
    print(i, type(i))

# 向集合中住家元素
vars.add('def')
print(vars)

# pop()从集合中任意删除一个元素 返回被删除的元素

# remove() 删除集合中的指定的元素 返回None 不存在则报错

# discard() 指定删除集合中的元素，不存在也不会报错

# clear() 清空集合

# update() 更新集合，把传入的多个参数元素添加到集合，重复的不添加

# 当前集合的浅拷贝，集合不存在深拷贝的问题
# vars = {1, 2, (1, [1, 2, 3])}
# print(vars)

"""
因为集合中不能存在列表元素，元组嵌套列表也不行(见上面案例)
而其他元素都是不可变的，所以不存在数据修改的操作
"""

# 冰冻集合
v = frozenset((1, 2, 3))
print(v)


# lesson 69
# 冰冻集合的定义

"""
语法：
    1.定义冰冻集合，只能使用其构造函数 frozenset() 函数来实现
    2.冰冻集合一旦定义不能修改
    3.冰冻集合只能做集合相关的运算：交差并补
    4.frozenset() 本身就是一个强制转换类型的函数，可以把其他类型容器的数据转化为冰冻集合
"""

vars = frozenset({1, 2, 3})
print(vars)


# 冰冻集合的推导式
vars = frozenset({i << 1 for i in range(6)})
print(vars)

# 冰冻集合可以普通集合一样进行交差并补运算

# lesson 70
vars1 = {1,2,3}
vars2 = {4,5,6}

newset = {i+j for i in vars1 for j in vars2}
print(newset)

newset = {i+j for i in vars1 for j in vars2 if i % 2 == 0 and j % 2 == 0}
print(newset)

# lesson 71
# 集合运算

"""
集合的主要运算
    交集 &
    并集 |
    差集 -
    对称差集 ^
"""

vars1 = {"郭富城", "刘德华", "张学友", "黎明"}
vars2 = {"尼古拉斯赵四", "刘能", "小沈阳", "宋小宝"}

newset = vars1 & vars2
print(newset)
newset = vars1 | vars2
print(newset)
newset = vars1 - vars2
print(newset)
newset = vars1 ^ vars2
print(newset)

# intersection(other) &    intersection_update(other)  &=  求交集 前者返回结果，后者更新对象的数据(修改数据源)
# union(other)  |       update(other)   |=                 求并集 '''''''
# difference(other)  -       difference_update(other)  -=  求差集 '''''''
# symmetric_difference(other) ^    symmetric_difference_update(other) ^=    求对称差集 '''''

# 子集 和 超集

# issuperset() 检测是否为超集
# issubset() 检测是否为子集

# isdisjoint 检测是否不相交，不相交返回True，相交返回False
