# lesson 65
# 字典定义


# 1. 使用{}定义
vardict = {'a': 1, 'b': 2, 'c': 2}
print(vardict)

# 2. 使用dict(keyword=v, keyword=v...) 函数定义
vardict = dict(name='zhangsan', sex='男', age=22)
print(vardict)

# 3. 数据类型的转换    列表或者元组，并且是二级容器
vardict = dict([['a', 1], ['b', 2]])
print(vardict)

# 4. zip压缩函数，dict转类型
var1 = [1, 2, 3, 4]
var2 = ['a', 'b', 'c', 'd']
vardict = dict(zip(var1, var2))
print(vardict)

# 获取元素
# dict["name"]

# 修改元素
# dict["name"] = value

# 删除元素
# del dict["name"]

# 添加元素
# dict["name"] = value 重复会被覆盖

# 成员检测
# res = value in dict
# res = value not in dict

# 获取当前字典的长度，多少个键值对
# res = len(dict)

# 获取当前字典中所有的key
# res = dict.keys()

# 获取字典中所有的value
# res = dict.values()

# 获取字典中所有的 键值对
# res = dict.items()

# 对字典进行遍历
# (1)
dic = {'a': 1, 'b': 2, 'c': 3}
for i in dic:
    print(i)
    print(dic[i])

# (2)
dic = {'a': 1, 'b': 2, 'c': 3}
for i, j in dic.items():
    print(i)
    print(j)


# lesson 66
# 字典相关函数

# len() 获取字典的键值对个数

# dict.keys()

# dict.values()

# dict.items()

# iter(d) 返回以字典的键为元素的迭代器
vardict = {'a': 1, 'b': 2, 'c': 3}
res = iter(vardict)
print(list(res))

# dict.pop(key)
# dict.popitem() 后进先出，把最后加入到字典的键值对弹出并返回一个元组
vardict = {'a': 1, 'b': 2, 'c': 3}
res = vardict.pop('a')
print(vardict)

# dict.clear() 清空字典

# dict.copy() 返回字典的浅拷贝

# dict.get()获取一个元素，存在则返回改键所对应的值，不存在默认返回None,也可以由第二参数指定返回内容
# 使用key获取字典中不存在的键值，会报错
vardict = {'a': 1, 'b': 2, 'c': 3}
res = vardict.get('bb', 'avvv')
print(res)

# dict.update()，更新字典,如key存在则更新，不存在就添加
res = vardict.update(a=11, b=22)
res = vardict.update({'c': 33, 'd': 44})
print(vardict)

# dict.setdefault(key[,default])
# 如果字典存在键 key，返回它的值。
# 如果不存在，插入值为 default 的键 key，并返回default
# default 默认为 None ,也可以用第二参数指定键值
vardict = {'a': 1, 'b': 2, 'c': 3}
res = vardict.setdefault('aa')
res = vardict.setdefault('bb', '111')
print(res)
print(vardict)

# lesson 67
# 字典推导式

# 下面，把字典中的键值对位置进行交换

# 1.普通方法实现
vardict = {'a': 1, 'b': 2, 'c': 3}
newdict = {}
for k,v in vardict.items():
    newdict[v] = k
print(newdict)

# 2.使用字典推导式实现
newdict = {v: k for k, v in vardict.items()}
print(newdict)

# 3.保留字典中偶数的键值，并且交换位置
print('='*20)
vardict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
newdict = {v: k for k, v in vardict.items() if v % 2 == 0}
print(newdict)

