# lesson 113 魔术方法2


"""
__len__
    触发机制：   当使用len函数去检测当前对象的时候自动触发
    作用:       可以使用len函数检测当前对象中某个数据的信息
    参数:       一个self 接收当前对象
    返回值:     必须有，并且是一个整型
    注意事项:   len要获取什么属性的值，就在返回值中返回哪个属性的长度即可

__str__
    触发机制：当使用str或者print函数对对象进行操作时自动触发
    作用：    代码对象进行字符串的返回，可以自定义打印的信息
    参数：    一个self，接收当前对象
    返回值：  必须有，而且必须是字符串类型的值

__repr__
    触发机制：在使用repr方法对当前对象进行转换时自动触发
    作用：    可以设置repr函数操作对象的结果
    参数：    一个self，接收当前对象
    返回值：  必须有，而且必须是字符串类型的值
    注意事项：正常情况下，如果没有__str__这个魔术方法，__repr__方法就会代替__str__魔术方法

__bool__
    触发机制：当使用使用bool函数检测当前对象时，自动触发
    作用：    可以代替对象进行bool类型的转换，可以转换任何数据
    参数：    一个self 接收对象
    返回值：  必须是一个布尔类型的返回值
"""

class Demo():
    listurl = [1,2,3]

    # 可以代替对象使用len函数，并返回一个指定的整型
    def __len__(self):
        return self.listurl.__len__()

    def __str__(self):      # 不支持隐式转换
        return "<这是当前脚本中的一个 对象>"

    def __repr__(self):
        return "这是一个对象 repr"

    def __bool__(self):
        return False

# 实例化对象
obj = Demo()
# res = obj.__len__()

# res = obj + "aaa"   # 报错
res = str(obj)
print(obj)

res = bool(obj)
print(res)








