# lesson 80 序列化-pickle

import pickle
"""
什么是序列化？为什么需要序列化？
1.序列化是指可以把python中的数据，以文本或二进制的方式进行转换，并且还能反序列化为原来的数据
2.一般来说数据在程序与网络中进行传输和存储时，需要以更加方便的形式进行操作，因此需要对数据进行序列化

pickle模块提供的函数
    dumps() 序列化，可以把一个python的任意对象序列化成为一个二进制
        pickle.dumps(arg)
    loads() 反序列化，可以把一个序列化后的二进制数据反序列化为python的对象
        pickle.loads(arg)
    
    dump() 序列化，可以把一个数据对象进行序列化并写入到文件中
        参数1. 需要序列化的数据对象
        参数2. 写入的文件对象
        pickle.dump(arg, fp)
    load() 反序列化，在一个文件中读取序列化的数据，并且完成一个反序列化
        参数1. 读取的文件对象
        pickle.load(fp)
"""

# vars = "i love you"     # b'\x80\x03X\n\x00\x00\x00i love youq\x00.'
vars = [1, 2, 3, 4]     # b'\x80\x03]q\x00(K\x01K\x02K\x03K\x04e.'
# vars = {"name": "张三", "age": 20, "sex": "m"}    # b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x06\x00\x00\x00\xe5\xbc\xa0\xe4\xb8\x89q\x02X\x03\x00\x00\x00ageq\x03K\x14X\x03\x00\x00\x00sexq\x04X\x01\x00\x00\x00mq\x05u.'

res = pickle.dumps(vars)
print(res, type(res))
pres = pickle.loads(res)
print(pres)

with open("./login.txt", 'wb') as fp:  # write() argument must be str, not bytes 所以必须用带b模式
    pickle.dump(vars, fp)

with open("./login.txt", 'rb') as fp:
    res = pickle.load(fp)
    print(res)

# lesson 81 序列化-json
"""
什么是json？
JSON（JavaScript Object Notation）
JSON 是一个受 JavaScript 的对象字面量语法启发的轻量级数据交换格式
JSON 在js语言中是一个对象的表示方法，和Python中的字典的定义规则和语法都很像
JSON 在互联网中又是一种通用的数据交换，数据传输，数据定义的一种数据格式

python中提供的json模块，可以把一些符合转换的python数据对象，转为json格式的数据
    json.dumps()    转换对象
    json.loads()
    
    json.dump()     转换对象并写入文件
    json.load()
"""

import json

# 一下语法格式定义的是一个 字典 数据类型
vardict = {"name": "admin", "age": 20, "sex": '男'}
vardict = [1,2,3,'男']
# vardict = 'abcd'
# vardict = 521

res = json.dumps(vardict)
print(res,type(res))
pyres = json.loads(res)
print(pyres)

with open("./login.txt", 'w') as fp:
    json.dump(res, fp)

with open("./login.txt", 'r') as fp:
    res = json.load(fp)
    print(res)


# lesson 82 数学模块 Math

import math

# math.cell() 向上取整，内置函数 round() 四舍五入

res = math.ceil(2.25)

# math.floor() 向下取整
res = math.floor(2.25)

# math.pow()
res = math.pow(2,3)

# math.sqrt() 开方运算
res = math.sqrt(9)

# math.fabs() 计算绝对值，结果是浮点数
res = math.fabs(-3.14)

# math.modf() 把一个数值拆分成整数和小数组成的元组
res = math.modf(3.1415)

# math.copysign(x,y) 把第二个参数的正负符号拷贝给第一个参数，结果为浮点数
res = math.copysign(-3, 99)

# math.fsum() 将一个容器类型数据中的元素进行一个求和运算，结果为浮点数
# res = math.fsum("123") # X  TypeError: must be real number, not str
# res = math.fsum({1,2,3}) # 注意：容器中的元素必须是可以运算的number类型

# math.factoria(x)
res = math.factorial(5)

# 常量
# 数学常数 π = 3.141592...，精确到可用精度
res = math.pi


# lesson 83 随机模块 random

import random

# random，random() 返回 0 - 1 之间的随机小数(左闭右开)
res = random.random()

# random.randrange ([开始值,]结束值[,结束值]) 随机获取指定范围内的整数
res = random.randrange(5)     # 一个参数，从0到整数之前的值，左闭右开
res = random.randrange(5, 8)  # 两个参数，从第一个值到第二个值之间的随机数，左闭右开
res = random.randrange(5, 10, 2)   # 三个参数，按照指定步进值从第一个值到第二个值之间的随机数，左闭右开

# random.randint() 随机产生指定范围内的随机整数
res = random.randint(5, 10)

# random.uniform() 获取指定范围内的随机小数
res = random.uniform(5, 10)

# random.choice() 随机获取容器类型中的值
res = random.choice('123')
res = random.choice([1,2,3,4])


# random.shuffle() 随机打乱当前列表中的值，没有返回值，直接打乱数据源
lst = [1, 2, 3, 4]
random.shuffle(lst)
print(lst)











