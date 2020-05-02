"""
方法的分类
1.对象方法
    特性：
        1.在类中定义的方法，含有self参数
        2.含有self的方法，只能使用对象进行调用
        3.该方法会把调用的对象传递进来
2.类方法
    特性：
        1.在类中定义的方法，使用类 @classmethod 进行装饰
        2.方法中有cls这个形参
        3.不需要实例化对象，直接使用类进行调用
        4.会把调用这个方法的类传递进来
3.绑定类方法
    特征：
        1.在类中定义的方法
        2.只能使用类进行调用
        3.不会传递对象或者类进来
4.静态方法
    特征：
        1.在类中定义的方法，使用了   装饰器 @staticmethod   进行了装饰
        2.可以使用对象或者类进行调用
        3.不会传递对象或者类进来
"""


class Demo():
    # 对象方法
    def func1(self):
        print(self)
        print("this is func1")

    # 类方法
    @classmethod
    def func2(cls):  # 方法传递类
        print(cls)
        print(" this is class function func2 ")

    # 绑定类方法
    def func3():
        print("this is bind class function func3")

    # 静态方法
    @staticmethod
    def func4():    # 所以不会传递对象或者类进来
        print("this is static method func4")


# 对象方法
obj = Demo()
# obj.func1()
# Demo.func1() # 不能直接使用类调用 对象方法
# Demo.func1('a') # 除非传递一个对象进去，不推荐


# 类方法
Demo.func2()  # 使用类直接调用
obj.func2()     # 即便使用对象进行调用，传递类进去的

# 绑定类方法
Demo.func3()    # 可以使用类调用绑定方法
obj.func3()     # 不能使用对象调用绑定方法

# 静态方法的调用
Demo.func4()
obj.func4()
