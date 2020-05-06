# lesson 115 成员相关魔术方法

"""
1.__getattribute__
    触发机制： 当访问对象成员时，自动触发，无论当前成员是否存在
    作用：     可以在获取对象成员时，对数据进行一些处理
    参数：     一个self，一个item接收当前访问的成员名称
    返回值：   可有可无，返回值就是访问的结果
    注意事项： 在当前的魔术方法中，禁止使用 对象.成员 的方式进行成员访问，会触发递归
              如果想要在当前魔术方法中访问对象的成员必须使用 object.__getattribute__ 来进行访问

2.__getattr__
    触发机制：  当访问对象中不存在的成员时，自动触发
    作用：      防止访问不存在的成员时报错，也可以为不存在的成员进行赋值操作
    参数：      一个self接收当前对象，一个item接收当前访问的成员名称
    注意事项：  当存在 __getattribute__ 方法时，会去执行 __getattribute__ 方法

3.__setattr__
    触发机制：  当给对象的成员进行赋值操作时会自动触发 (包括添加，修改)
    作用：     可以限制或管理对象成员的添加和修改操作
    参数：     1.self接收当前对象  2.设置的成员名 3.设置的成员值
    返回值：   无
    注意事项： 在当前的魔术方法中禁止给当前对象的成员直接进行赋值操作，会触发
              如果想要给当前对象的成员进行赋值，需要借助 object
              格式：  object.__setattr__(self,item,value)

4. __delattr__
    触发机制： 当删除对象成员时自动触发
    作用：     可以去限制对象成员的删除，还可以删除不存在成员时防止报错
    参数：     1.self 接收当前对象   2.item 删除的成员名称
    返回值：   无
    注意事项： 在当前魔术方法中禁止直接删除对象的成员，会触发递归操作。
              如果想要删除当前对象的成员，那么需要借助 object
              格式： object.__delattr__(self,item)

5.访问成员的顺序
    1.调用__getattribute__魔术方法
    2.调用数据描述符
    3.调用当前对象的成员
    4.调用类的成员
    5.调用非数据描述符
    6.调用父类的成员
    7.调用__getattr__魔术方法
"""

# 定义类
class Person():
    # 属性成员
    name = "名字"
    age = "年龄"
    sex = "性别"

    # 方法成员
    def __init__(self, n="张三丰", a=180, s="男"):
        self.name = n
        self.age = a
        self.sex = s

    def say(self):
        print("聊聊人生，谈谈理想。。。")
    def sing(self):
        print("高歌一曲。。。")

    获取对象成员时自动触发
    def __getattribute__(self, item):
        # 在方法中使用object来获取属性值
        res = object.__getattribute__(self, item)
        # 在方法中可以对访问的成员数据进行处理
        return res[0]+'*'+res[2]

    # 当访问的成员不存在时，自动触发
    def __getattr__(self, item):
        print("成员不存在,进行赋值")
        object.__setattr__(self, item, "dongsen")
        return False

    # 当给对象成员进行赋值时触发，注意该方法中如果没有给对象成员赋值，那么对象成员赋值失败
    def __setattr__(self, key, value):
        print(self, key, value)
        object.__setattr__(self, key, value)

    # 当删除成员时自动触发
    def __delattr__(self, item):
        print(item)
        object.__delattr__(self, item)

# 实例化对象
zs = Person()
print(zs.name)

zs.n = "aaaaa"
print(zs.n)

del zs.n
print(zs.n)

