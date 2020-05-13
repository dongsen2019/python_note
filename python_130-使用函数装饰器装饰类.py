# lesson 130 使用函数装饰器装饰类

"""
还有一种装饰器，是专门装饰类的。也就是在类的定义的前面用@装饰器这种语法
@装饰器
class Demo():
    pass

装饰器给函数进行装饰，目的是不改变函数调用和代码的情况下给原函数增加了新的功能。

装饰器给类进行装饰，目的是不改变类的定义和调用的情况下给类增加新的成员（属性或方法）
"""

# 使用函数装饰器，给类进行装饰，增加新的属性和方法

# 定义函数，接收一个类。返回修改后的类
def kuozhan(cls):
    def func2():
        print("我是在装饰器中追加的新方法，func2")
    cls.func2 = func2   # 为cls增加方法成员
    cls.name = "我是在装饰器中追加的新属性 name"

    # 返回时，把追加类新成员的 类 返回去
    return cls


@kuozhan  # kuozhan(Demo) ==>   cls(Demo) 增加成员func2和属性name ==> 再把cls(Demo)赋值给Demo
class Demo():
    def func():
        print("我是Demo类中定义的func方法")

Demo.func()
Demo.func2()
print(Demo.name)

