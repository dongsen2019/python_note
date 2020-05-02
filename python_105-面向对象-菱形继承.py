# lesson 105 面向对象-菱形继承


"""
    A
  B   C
    D
"""

# 祖先类
class HuMan():
    num = 111

    def eat(self):
        print("顿顿都是小烧烤。。。")

# 父亲类
class F(HuMan):
    num = 222

    def eat(self):
        super().eat()
        print(super().num)
        print("大口喝酒，大口吃肉。。。")

# 母亲类
class M(HuMan):
    num = 333

    def eat(self):
        super().eat()
        print(super().num)
        print("动作优雅，浅尝即止。。。")

# 孩子类
class C(F,M):
    num = 444

    def eat(self):
        super().eat()
        print(super().num)
        print("吃也哭，不吃也哭。。。")


"""
顿顿都是小烧烤。。。
111
动作优雅，浅尝即止。。。
333
大口喝酒，大口吃肉。。。
222
吃也哭，不吃也哭。。。
"""


print(C.mro())
"""
[<class '__main__.C'>, <class '__main__.F'>, <class '__main__.M'>, <class '__main__.HuMan'>, <class 'object'>]
"""

"""
https://www.cnblogs.com/whatisfantasy/p/6046991.html    MRO C3算法
https://www.jianshu.com/p/de7d38c84443
"""
c = C()
c.eat()

"""
super()
    使用super去调用父级的方法时，实际上是在用super调用MRO列表中的上一级中的方法
    使用super去访问父级的属性时，实际上是在用super访问MRO列表中的上一级中的属性
super()本身调用基类方法时，传递self对象，在方法中使用self就是调用方法的对象自己本身
"""
