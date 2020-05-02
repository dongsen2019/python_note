# lesson 104 多重继承


"""
一个类去继承多个父类的方式

语法格式：
    class father():
        pass

    class mother():
        pass

    class son(father,mother):
        pass
"""

# 父亲类

class F():

    def eat(self):
        print("大口喝酒，大口吃肉。。。")


# 母亲类

class M():

    def eat(self):
        print("动作优雅，浅尝即止")

# 孩子类
class C(F, M):

    def eat(self):
        super().eat()   # 多继承和多继承中的父类方法的调用
        print("吃也哭，不吃也哭。。。")


# 实例化对象
c = C()
c.eat()
print(C.mro())      # 调用mro列表方法是类方法不是对象方法
"""
[<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class 'object'>]
"""