# lesson 98

"""
成员方法中的self
    1.self在方法中只是一个形参，并不是关键字
    2.self在方法中代表的事当前这个对象自己
    3.self在方法中代表对象可以去操作成员、可以使用self在类的内部访问成员
方法的分类
    1.含有self或者可以接受对象作为参数的方法：非绑定方法
    2.不含self或者不能接受对象作为参数的方法：绑定类方法

    非绑定类方法，可以使用对象去访问
    绑定类方法，可以使用类去访问
"""


# 定义人类
class Person():
    # 成员属性
    name = "名字"
    age = "年龄"
    sex = "性别"

    # 成员方法
    def sing(self):
        print("会唱。。。")

    def dance(self):
        print("会跳。。。")

    def rap(self):
        print("会rap。。。")

    def func(self):
        # 测试，在类的内部是否可以像类的外部一样，去访问和操作成员
        print(self)
        print(self.name)  # 访问对象的属性
        self.name = "张三三"  # 修改对象的属性
        self.sanwei = "80 80 80"  # 添加对象的属性
        print(self.sanwei)
        self.rap()  # 调用对象的方法
        # 只要是对象能干的事，self都可以代表对象去完成
        # 比如：成员的所有操作(添加，删除，更新，访问，调用。。)

    def func2():
        print("这是类方法。。。")


# 实例化对象
zs = Person()
zs.func()
print(zs.name)
del zs.name
print(zs.name)
Person.rap()


"""
self 单词本身的意思 自己
self 在类的方法中 代表 当前这个对象
self 代表调用这个方法的对象，谁调用了这个方法，self就代表谁
self 就可以在类的内部代替对象进行各种操作

如果在类中定义的方法不含self这个形参时(self形参，包括其它的代表都不可以)
那么这个方法就不能使用对象去调用
不含self形参的方法，只能使用类去调用
这种不接受对象作为形参的方法，叫做绑定类方法
"""


