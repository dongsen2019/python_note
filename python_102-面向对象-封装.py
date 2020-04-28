# lesson 102 封装

# 封装
"""
封装就是使用特殊的语法，对成员属性和成员方法进行包装，达到保护和隐藏的目的。
但是封装是为了限制一些访问和操作，但是不能全部都限制（不能不让使用）
被封装的成员只是限制了访问的权限，并不是不让访问
通常情况下，被封装的成员主要是供内部使用
"""

# 封装的级别
"""
被特殊语法封装的成员，会有不同的访问的权限

封装的级别
    成员      ==>     公有的
    _成员     ==>     受保护的    (约定俗成，而python没有具体实现)
    __成员    ==>     私有的
            公有的 public      受保护的 protected      私有的 private
在类的内部       OK                  OK                      OK
在类的外部       OK                  No(python可以)          No

了解即可：
在python中给成员进行私有化，其实就是改了成员的名字
私有化 ==> _类名__成员

"""


class Person():
    # 成员属性
    name = None     # public
    _age = None     # protected
    __sanwei = None   # private

    def __init__(self, n, a, s):
        self.name = n
        self._age = a
        self.__sanwei = s

    # 成员方法
    def say(self):
        print("聊聊人生和理想。。。")

    def sing(self):
        print("高歌一曲，豪放一生。。。")

    def kiss(self):
        print("打个kiss。。。")


# 实例化对象
ym = Person("杨幂", 28, "60,50,60")

print(ym._age)    # 在类的外部不能操作，受保护的成员 （但是python中可以）
# print(ym.__sanwei)  # 在类的外部不能操作，私有成员属性

print(ym._Person__sanwei)  # 可以使用特殊的语法获取私有成员

# ym._sing()    # ok
# ym.__kiss()   # X  在类的外部不能操作，私有成员属性

# 查看对象的所有成员
print(ym.__dict__)  # 可以获取当前对象的所有属性
print(Person.__dict__) # 可以获取当前类的所有成员信息

