# lesson 11
# 集合的定义方式
s1 = {1, 2, 3}
s2 = set([1, 2, 3])
print(s1)
print(s2)

# 特别的,如果要定义一个空集合，需要用set(),因为使用{}定义，会是一个空的字典
s1 = {}
print(s1, type(s1))
s2 = set()
print(s2, type(s2))

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
# 容器类型的转换函数只能转换可迭代的数据类型（容器类型的构造函数只能接受一个参数，而且必须是可迭代的数据类型参数）
'''
list()
tuple()
dict()
set()
'''
# 其中dict()只能转换二维数据类型，每个元素的第一维度为键,第二维度为值
# 以list为元素不能构建集合(唯独可以使用集合的构造函数传递列表(可迭代对象)),因为list类没有定义hash算法
# 不能用集合元素构造字典和集合，un-hashable
a = {{1, 2}, {3, 4}}
print(dict(a))

# lesson 15
# and   or    not
print(40 and 30)  # 30
print(10 or 20)   # 10
print(0 or 10)  # 10
print(not 10)  # false

# lesson 17
# 成员运算符：in    not in
# 身份运算符：is    is not  比较两个对象是不是同一个内存地址
s = "dongsen"
print('gs' in s)



