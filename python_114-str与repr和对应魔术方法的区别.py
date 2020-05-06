# lesson 114  str和repr的区别


"""
str和repr函数都能够把其他类型的数据转为字符串类型
str函数会把对象 转为 更适合人类阅读的形式
repr函数会把对象 转为 解释器读取的形式
如果数据对象并没有更明显的区别的话，str和repr的结果是一样的
"""

s = "521"
r1 = str(s)
r2 = repr(s)
print(r1, type(r1))
print(r2, type(r2))

# 521 <class 'str'>
# '521' <class 'str'>