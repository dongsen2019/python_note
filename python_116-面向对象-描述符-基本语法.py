# lesson 116 描述符-基本语法


"""
描述符：
    当一个类中，包含了三个魔术方法(__get__，__set__，__delete__)之一，或者全部时，那么这个类就称为描述符类
作用：
    描述符的作用就是对一个类的某个成员进行一个详细的管理操作（获取，赋值，删除）
    描述符就是代理了一个类中的成员的操作，描述符属于类，只能定义为类的属性

使用格式
    把当前的描述符类赋值给一个需要代理的类中的成员属性

一个类中的成员的值是另一个描述符类的对象
那么当这个类中的成员进行操作时，就是对另一个对象操作
"""

# 定义描述符类
class PersonName():
    __name = 'name'

    def __get__(self, instance, owner):
        # print(self, instance, owner)
        # <__main__.PersonName object at 0x000000000287B710>
        # <__main__.Person object at 0x00000000029A9B00>
        # <class '__main__.Person'>
        return self.__name

    def __set__(self, instance, value):
        print(self, instance, value)
        # <__main__.PersonName object at 0x00000000023A9B38>
        # <__main__.Person object at 0x0000000001E2B710>
        # 张三
        self.__name = value

    def __delete__(self, instance):
        print("不允许删除")

# 定义普通的类
class Person():
    # 把类中的一个成员属性交给一个描述符类来实现
    # 一个类中的成员的值是另一个描述符类的对象
    # 那么当这个类中的成员进行操作时，就是对另一个对象操作
    name = PersonName()


# 实例化对象
zs = Person()
print(zs.name)
zs.name = "张三"
print(zs.name)
del zs.name
print(zs.name)
