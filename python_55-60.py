# lesson 55
# 列表的定义

"""
1.可以使用中括号进行定义[]
2.也可以使用list函数 定义
3.在定义列表的元素时，需要在每个元素之间使用逗号，进行分隔。[1,2,3,4]
4.列表中的元素可以是任意类型的，但通常是用于存放同类项目的
"""

lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd']

# '+'拼接运算符
print(lst1+lst2)

print(lst1+lst2+[11,22,33])

# '*'重复运算符
print(lst1*3)

# []索引运算符

# 不能通过下标添加元素

# list.append() 在列表尾部添加元素
lst1 = [1, 2, 3, 4]
lst2 = ['a', 'b', 'c', 'd']
lst2.append('ff')
print(lst2)

# list.pop()默认删除尾部元素，可以输出索引号删除指定元素
lst2.pop()
print(lst2)

# len(list) 或者 list.__len()__
print(len(lst2))

# lesson 56
# 列表的切片操作

"""
语法 ==> 列表[开始索引:结束索引:步进值]
        1.列表[开始索引:]  ==> 从开始索引到列表的最后
        2.列表[:结束值]    ==> 从开始到指定的结束索引之前
        3.列表[:] 与 [::] ==>默认值[0:超尾迭代器:1]  所有列表元素的切片
        4.列表[-1::-1] 或 [::-1]倒序输出
"""

lst = [0, 1, 2, 3, 4, 5, 6, 7]
print(lst[0:6])
print(lst[2:])
print(lst[:4])
print(lst[-1::-1])

# 使用切片 对列表数据进行更新和删除
# 将指定的切片替换为对应的数据（可迭代类型对象，拆分每个元素进行赋值）
lst[2:5] = 'abc'  # 容器元素无论多于或少于切片元素，这些元素都占用切片位置
lst[2:7:2] = [11, 22, 33]  # 该方式，容器元素数量必须与切片元素数量相等
print(lst)

# 删除切片元素
lst = [0, 1, 2, 3, 4, 5, 6, 7]
del lst[2:7:2]
print(lst)

# lesson 57
# list相关方法

# list.insert()在指定的索引位置添加新元素
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst.insert(1,'a')
print(lst)

# list.pop() 出栈操作，弹出最后元素，返回出栈元素
#            也可以指定索引号的元素出栈
lst = [0, 1, 2, 3, 4, 5, 6, 7]
print(lst.pop())
lst.pop(1)
print(lst)

# list.remove(x) 删除list中第一个 list[i] 等于 x 的项目。
#                如果找不到该内容的元素，则报错
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst.remove(5)
print(lst)
# list.remove(9) # ValueError: list.remove(x): x not in list


# list.index(x[,start[,end]]) 查找指定元素在列表中第一次出现的索引位置
#                             也可以在指定的区间内查找,找不到报错
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst.index(7)
# print(lst.index(6,1,6))  # ValueError: 6 is not in list

# extend() 延展容器，接收一个容器类型的数据，把容器中的元素追加到元列表中
lst = [0, 1, 2, 3, 4, 5, 6, 7]
lst.extend((2,3,4))
print(lst)

# clear() 清空列表

# reverse() 列表翻转

# sort()  和通用算法sorted()区别就是，sorted()返回一个排序后的副本
# 方法和sorted()一样
lst = [6, -1, 8, -3, 9, -5, 6, 7]
lst.sort(key=abs, reverse=True)
print(lst)

# copy() 拷贝，复制当前的列表，制作一份副本

lst = [1, 2, 3]
res = lst.copy()
del res[1]
print(lst)
print(res)

"""
对于一维列表这样删除副本内容不影响原数据内容
对于二维列表这样操作则不行
"""

# 二维列表
lst = [1, 2, 3, [11, 22, 33]]
res = lst.copy()
print(lst[3], id(lst[3]))
print(res[3], id(res[3]))
del res[3][1]
print(lst)
print(res)

"""
原因可能是copy()方法只是复制了列表的地址
"""

# lesson 58
# 深度复制
lst = [1, 2, 3, [11, 22, 33]]
res = lst.copy()
res[3] = lst[3].copy()
del res[3][1]
print(lst)
print(res)

# 可以使用 copy 模块简化操作深度拷贝
import copy
lst = [1, 2, 3, [11, 22, 33]]
res = copy.deepcopy(lst)
print(lst[3], id(lst[3]))
print(res[3], id(res[3]))
# [11, 22, 33] 55148744
# [11, 22, 33] 55169608

# lesson 59
# 列表推导式

# 普通方法
lst = []
for x in range(0, 10):
    lst.append(x**2)
print(lst)

# 使用map函数和list完成
lst = list(map(lambda x: x**2, range(0, 10)))
print(lst)

# 使用列表推导式完成
lst = [i**2 for i in range(10)]
print(lst)

# 列表推导式案例1
str1 = '1234'
lst = [int(x)*2 for x in str1]
print(lst)

# 带有判断条件的列表推导式
# [含x的处理表达式 for x in 迭代对象 if判断表达式]

lst = [x for x in range(10) if x % 2 == 0]
print(lst)


# 带有条件判断的多循环的推导式
# [1,2,3],[3,1,4] ==> 求笛卡尔积

lst = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4]]
print(lst)

# 列表的嵌套推导式

# 行列转置
lst = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

res = [[row[i] for row in lst] for i in range(0, 4)]
print(res)



