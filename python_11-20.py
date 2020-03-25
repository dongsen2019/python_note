# lesson 11
# 集合的定义方式
s1 = {1,2,3}
s2 = set([1,2,3])
print(s1)
print(s2)

# 特别的,如果要定义一个空集合，需要用set(),因为使用{}定义，会是一个空的字典
s1 = {}
print(s1,type(s1))
s2 = set()
print(s2,type(s2))

# 集合主要用于运算,交集,差集,并集和对称集合
a = {1, 2, 3, 'a', 'b'}
b = {1, 'a', 22, 33}

# 交集 {1, 'a'}
print(a & b)
# 差集 {2, 3, 'b'}
print(a - b)
# 并集  {1, 2, 3, 33, 22, 'a', 'b'}
print(a | b)
# 对称集合 {2, 33, 3, 'b', 22}
print(a ^ b)

# lesson 12
# 数据类型转换函数汇总

'''
str()
int()
float()
bool()
list()
tuple()
dict()
set()
'''

# lesson 13
# 容器类型转换函数汇总
# 容器类型的转换函数只能转换可迭代的数据类型（容器类型的构造函数只能接受可迭代的数据类型参数）
'''
list()
tuple()
dict()
set()
'''

