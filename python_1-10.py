# lesson 5
# python语法数据交换的技巧

a = 10
b = 20
print(a, b)
a, b = b, a
print(a, b)

# lesson 6
# 关于python的引号嵌套规则,单双引号互相嵌套,嵌套不能用同一种引号

s1 = "I 'love' you"
s2 = 'I "love" you'

print(s1)
print(s2)

# 如果需要打印的字符串换行,可以使用\换行符或者只用三引号''' '''

s1 = "I love" \
        " you"
s2 = '''I love
you'''

print(s1)
print(s2)

# 在定义元祖时, 如果只有一个元素, 要在元素后加一个逗号

a = ('abc')
b = ("abc", )

print(a, type(a))
print(b, type(b))

# lesson 10
# dict的键名不能重复,否则后面的定义会覆盖前面的定义
# 字典的底层实现是无序的

a = {'a': 10, 'b': 20, 'c': 30, 'a': 40}
print(a['a'])



