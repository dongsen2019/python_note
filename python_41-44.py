# lesson 41
# range() 函数

"""
range(start, stop[,step])函数
功能：能够生成一个指定的数字序列
参数：
    start: 开始的值，默认值为0
    stop : 结束的值
    [,step]: 可选，步进值 默认值为1
返回值：    可迭代的对象，数字序列
"""

# range()可迭代，所以可以转化为list()，也可以用iter()转化为迭代器

# lesson 42
# zip函数

"""
zip()
功能：zip 函数是可以接受多个可迭代的对象，然后把每个可待跌对象中的第i个元祖组合在一起，
直到最短的一个可迭代输入被耗尽时，迭代器终止。返回一个元祖的迭代器
参数：*iterables，任意个可迭代对象
返回值： 返回一个元祖的迭代器
"""

var1 = '1234'
var2 = ['a', 'b', 'c', 'd']
var3 = ('A', 'B', 'C', 'D')

res = zip(var1, var2, var3)
for i in res:
    print(i)

# 输出:
# ('1', 'a', 'A')
# ('2', 'b', 'B')
# ('3', 'c', 'C')
# ('4', 'd', 'D')

tup = (1,2,3)
lst = list(tup)
print(lst)

# zip()与*运算符一起可用于解压缩列表：
x = [1, 2, 3]
y = [4, 5, 6]
zipped = zip(x, y)
list(zipped)
x2, y2 = zip(*zip(x, y))
print(x == list(x2) and y == list(y2))

# lesson 43
# 数据类型转换相关内置函数

"""
int()  将其他类型数据转为整数
float() 转为浮点类型
bool()  转为布尔类型
complex()  转为复数
str()   转为字符串类型
list()  转为列表类型
tuple() 转为元祖类型
dict()  转为字典类型
set()   转为集合类型
"""


# 变量相关函数

"""
abs() 绝对值
sum()
max()
min()
pow() 乘方运算
round() .5(舍入距离相同时)，奇进偶退
"""

# lesson 44
# 进制函数

# bin() 转为二进制
print(bin(123))
print(int(0b1111011))

# oct() 转为八进制
print(oct(123))
print(int(0o173))

# hex() 转为十六进制
print(hex(123))
print(int(0x7b))

# ord() 将字符转为ascii
r = ord('a')
print(r)

# chr() 将ascii转为字符
r =chr(65)
print(r)
