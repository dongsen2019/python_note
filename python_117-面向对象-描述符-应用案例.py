# lesson 117 描述符应用案例
# 定义一个学生类，需要记录 学院的id，名字，分数

"""
# 要求：学员的分数只能在0-100范围中
解决方法：
    1.在__init__方法中检测当前分数范围
        # 检测分数范围
        if score >= and score <=100:
            self.score = score
    这个解决方案只能在对象初始化时有效。
    2.定义一个setattr魔术方法进行检测
        在给score分数进行赋值时，进行分数的检测判断

        if key == "score":
            if value >= 0 and value <= 100:
                object.__setattr__(self, key, value)
            else:
                print("score为负数，设置为0")
                object.__setattr__(self, key, 0)
        else:
            object.__setattr__(self, key, value)

问题2：假如学员的分数不止一个时怎么办，比如 语文分数，数学分数，英语分数
      另外就是当前这个类中的代码是否就比较多了呢？

    3.可以使用描述符来代理我们的分数这个属性
        1.定义Score描述符类
        2.把学生类中的score这个成员交给描述符类进行代理
        3.只要在代理的描述符类中对分数进行赋值和获取就可以了
"""

class Student():
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        """
        使用__setattr__时，init中的相应对象赋值也要使用
        object.setattr(self, key, value),否侧会造成无限递归
        *** self.score中的score类型一定是字符串 ***
        """
        if score >= 0 and score <= 100:
            object.__setattr__(self, "score", score)
        else:
            print("score为负数，设置为0")
            object.__setattr__(self, "score", 0)

    def returnMe(self):
        info = f"""
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        """
        print(info)

    def __setattr__(self, key, value):
        # 检测是否是给score进行赋值操作
        """
            使用__setattr__时，init中的相应对象赋值也要使用
            object.setattr(self, key, value),否侧会造成无限递归
        """
        if key == "score":
            if value >= 0 and value <= 100:
                object.__setattr__(self, key, value)
            else:
                print("score为负数，设置为0")
                object.__setattr__(self, key, 0)
        else:
            object.__setattr__(self, key, value)

# 实例化对象
# zs = Student(1011, "张三", 80)
# zs.returnMe()
#
# zs.score = 200
# zs.returnMe()


# 使用描述符方案

# 定义描述符类 代理分数的管理
class Score():
    __score = 0
    def __get__(self, instance, owner):
        return self.__score

    def __set__(self, instance, value):
        if value >= 0 and value <= 100:
            self.__score = value
        else:
            print("score为负数，设置为0")
            self.__score = 0

# 使用描述符代理score分数属性
class Student():
    score = Score()
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score

    def returnMe(self):
        info = f"""
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}
        """
        print(info)

zs = Student(1011, "张三", 80)
zs.returnMe()


