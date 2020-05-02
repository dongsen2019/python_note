# lesson 106 继承关系检测


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


# 检测一个类是否是另一个类的子类
res = issubclass(C, HuMan)      # True
res = issubclass(F, HuMan)      # True
res = issubclass(C, M)          # True
res = issubclass(HuMan, C)      # False

print(res)

