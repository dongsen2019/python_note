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

