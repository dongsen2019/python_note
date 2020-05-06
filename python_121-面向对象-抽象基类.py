# lesson 121 抽象类


"""
抽象类是一个特殊的类：
    1.抽象类不用作实例化
    2.抽象类中包含了抽象方法，抽象方法就是没有实现代码的方法
    3.抽象类需要子类继承，并重写父类的抽象方法，才可以使用

抽象类，一般应用在程序设计，程序设计中一般是要对功能和需求进行规划，其中一些需求是明确的并且可以完成的，
但是也可能会有一些需求是不明确的，或者不确定具体需要怎么实现，那么此时就可以把这个不确定怎么实现或者需
要后面需要后面再去实现的方法，定义为抽象方法（只定义方法名，不写具体代码）

举例：
    公司有一项新的产品需要开发，交给了开发部门的老大
    这个老大开始会规划设计怎么去完成这个产品的开发，
    必须项目需要用到不同的技术，需要不同的人来完成，
    这样的话，老大就自己完成了一部分功能，还有一部分定义了需求，
    但是没有具体实现，需要其他的人来实现

    这样，已经完成的部分就是 普通方法，定义了但是未完成的就可以理解为 抽象方法
"""

import abc
# 如果要定义为抽象类，那么这个类的 metaclass属性必须是metaclass=abc.ABCMeta
class WriteCode(metaclass=abc.ABCMeta):

    # 需要抽象的方法，使用装饰器进行装饰
    @abc.abstractmethod
    def write_c(self):
        pass

    def write_java(self):
        print("实现了java代码的开发")

    def write_python(self):
        print("实现了python代码的开发")


# 抽象类不能直接实例化对象
# obj = WriteCode() # TypeError: Can't instantiate abstract class WriteCode with abstract methods write_c


# 定义子类，继承抽象类，并实现抽象类中的抽象方法
class Demo(WriteCode):
    def write_c(self):
        print("实现了c代码的开发")


obj = Demo()
obj.write_c()