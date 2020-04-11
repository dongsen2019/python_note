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