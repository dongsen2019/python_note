# lesson 49
# 字符串-转义字符

"""
1.单引号定义字符串''
2.双引号定义字符串""
3.三引号定义字符串''' ''' 或者 """ """
4.字符串定义时，引号可以互相嵌套
"""

# 转义字符
"""
\  代码换行符
\n 换行符
\r 回车符
\t 水平制表符
\b 退格符
\\ \符号
"""

'''
如果不西欧昂让字符串转义，可以在字符串的前面加上r (r" ")
'''
# lesson 50
# 字符串相关方法

"""
字符串的[]下标运算符
字符串的"+"运算符 拼接
字符串的"*"运算符 重复拼接
字符串的[起始值:结束值:步进（默认为1，负数为从右到左）]切片运算符 起始下标为0，结尾下标为-1
        [::] 从头到尾，步进为1
        [::-1] 字符串倒转
"""
from functools import reduce

str1 = "dongsen"
print(str1)
lst = list(str1)
lst[0] = 'D'
res = reduce(lambda x, y: str(x) + str(y), lst)
print(res, type(res))
print(str1[-1:-100:-1])

# lesson 51
# format() 格式化字符串   f

# 1 普通方式
a = "李白"
s1 = "{}乘舟将欲行，忽闻岸上踏歌声".format(a)
s2 = "{}乘舟将欲行，忽闻岸上{}".format(a, '踏歌声')
print(s1, s2)

# 2 通过索引传参
s2 = "{2}乘舟将欲行，忽闻岸上{1}".format('a', 'b', 'c')
print(s2)

# 3 关键字传参
s2 = "{a}乘舟将欲行，忽闻岸上{b}".format(a="李白", b="踏歌声")
print(s2)

# 4 容器类型数据传参
"""
解包后是一维数组：list使用索引号（0,1,2...）
                dict使用键名
未解包是二维数组：使用二维下标0[0],0[1]...
                            0[键名1]...
"""
# list
lst1 = ["李白", "辛弃疾", "好丽友"]
s2 = "豪放派:{0}， 婉约派:{1}，蛋黄派:{2}".format(*lst1)
print(s2)

# dict
dic1 = {'a': '辛弃疾', 'b': '好丽友'}
s2 = "豪放派:{0[a]}，蛋黄派:{0[b]}".format(dic1)
print(s2)

# python3.7新增的方法 f
s2 = f"豪放派:{dic1['a']}，蛋黄派:{dic1['b']}" # 注意单双引号互相嵌套
print(s2)

# lesson 52
# 字符串函数-1-英文字符与字符检测相关函数

# str.capitalize() 返回原字符串的副本，其首个字符大写，其余为小写
varstr = 'i love you'
res = varstr.capitalize()
print(res, type(res))

# str.title() 返回原字符串的标题版本，其中每个单词第一个字母为大写，其余字母为小写。
varstr = 'i love you'
res2 = res.title()
print(res2)

#str.upper() str全转为大写

#str.lower() str全转为小写

# str.swapcase() 返回原字符串的副本，其中大写字符转换为小写，反之亦然。
#                请注意 s.swapcase().swapcase() == s 并不一定为真值。

str1 = "dongsen"
str2 = str1.swapcase().swapcase()
print(str2)
print(str1 == str2)

print(str1.isalnum())

# str.isupper() 测当前的字符串中的英文字符是否 全部 由大写组成

# str.islower() 检测当前的字符串中的英文字符是否 全部 由小写组成

# str.istitle() 检测当前的字符串中的英文字符串是否符合title标题的要求

# str.isalnum() 检测字符串是否都由(中文，英文字符，数字)组成

# str.isalpha() 检测字符串是否由（中英文字符）组成

# str.isdigit() 检测字符串是否由数字组成

# str.isspace() 检测是否为空格字符

# str.startswith(prefix[, start[, end]])
"""
如果字符串以指定的 prefix 开始则返回 True，否则返回 False。 
prefix 也可以为由多个供查找的前缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 
如果有可选项 end，将在所指定位置停止比较。
"""
print(str1.startswith('ong',1,4))

# str.endswith(suffix[, start[, end]])
"""
如果字符串以指定的 suffix 结束返回 True，否则返回 False。 
suffix 也可以为由多个供查找的后缀构成的元组。 如果有可选项 start，将从所指定位置开始检查。 
如果有可选项 end，将在所指定位置停止比较。
"""

print(str1.endswith('se',1,6))

# lesson 53
# 字符串查找  重点

strr1 = "dongsendeng"
print('111')
print("dong" in strr1)
print(strr1.__len__())

#  str.find(sub[, start[, end]]) 返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。
#                                可选参数 start 与 end 会被解读为切片表示法。 如果 sub 未被找到则返回 -1。
res = strr1.find("d")
print(res)
res = strr1.find("d",1,11)
print(res)
# str.rfind(sub[, start[, end]]) 从右往左 获取指定字符在字符串中第一次出现的位置索引，未找到则返回-1
res = strr1.rfind('d')
print(res)
res = strr1.find("d",0,7)
print(res)

# str.index()、str.rindex() 和 find 方法一样，只不过如果没有找到则报错
res = strr1.count('d')
print(res)

# lesson 54
# 字符串操作相关函数 重点

st = "user_admin_id_123"

# str.split() 按照指定的字符进行分隔，把一个字符串分隔成一个列表
res = st.split('_') # ['user', 'admin', 'id', '123']
print(res)

st = "uid=123&type=ab&kw=hh"
res = st.split('&') # ['uid=123', 'type=ab', 'kw=hh']
print(res)
lst = []
for i in res:
    r = i.split('=')
    lst.append(r.pop())
print(lst)

# str.split()还可以指定分隔的次数
st = "user_admin_id_123"
res = st.split('_',2)
print(res)

res = st.rsplit('_',2)
print(res)

# str.join() 按照指定的字符，把容器类型中的数据接成一个字符串
arr = ['user', 'admin', 'id', '123']

res = '&'.join(arr)
print(res)

# str.strip() 可以去除字符串左右两侧的指定字符
vars = "###这是一个文章的标题##"
res = vars.strip('#')
print(res)

res = vars.lstrip('#')
print(res)
res = vars.rstrip(('#'))
print(res)

# str.replace() 替换
vars = "dongsendongsendongsen"
print(vars.replace("dong", "DONG"))
print(vars.replace("dong", "DONG",2))

# str.center() 字符串居中，两侧填充字符
vars = "dancing"
print(vars.center(20, '*'))
print(vars.ljust(15, '*'))
print(vars.rjust(15, '*'))

