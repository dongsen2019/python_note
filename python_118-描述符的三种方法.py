# lesson 118 描述符的三种定义方法


# 格式一 通过定义 描述符类来实现
class ScoreManage():
    def __get__(self, instance, owner):
        pass
    def __set__(self, instance, value):
        pass
    def __delete__(self, instance):
        pass


class Student():
    score = ScoreManage()


# 格式二 使用 property 函数 来实现
class Student():

    # 在当前需要被管理的类中 直接定义类似下面三个方法
    def getscore(self):
        print("getscore")

    def setscore(self, value):
        print("setscore", value)

    def delscore(self):
        print("delscore")


    # 在函数中指定对应的三个方法,对应的方法 1.__get__,2.__set__,3.__delete__
    score = property(getscore, setscore, delscore)

zs = Student()
print(zs.score)
zs.score = 200
del zs.score


# 格式三 使用 @property 的装饰器语法来实现
class Student():
    __score = None

    @property
    def score(self):
        print("get")
        return self.__score

    @score.setter
    def score(self, value):
        print("set")
        self.__score = value

    @score.deleter
    def score(self):
        print("delete")
        del self.__score

zs = Student()
print(zs.score)
zs.score = 199
print(zs.score)