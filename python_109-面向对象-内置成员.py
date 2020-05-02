# lesson 109
# 内置成员

class A():
    pass

class B():
    pass

class C():
    pass


class Demo(A, B, C):
    """
     此处是类的说明文档
    """
    name = 'a'
    age = 20

    def say(self):
        print("会说会唱会rap。。。")


obj = Demo()
obj.san = "aaa"

# 获取类/对象的所属成员
res = Demo.__dict__     # 获取当前类的所属成员
res = obj.__dict__      # 获取当前对象的所属成员

# 获取类/对象的文档信息
res = Demo.__doc__
res = obj.__doc__

# 获取类名组成的字符串
res = Demo.__name__

# 获取类所在的文件名称，如果是当前文件，显示为__main__
res = Demo.__module__

# __bases__ 获取当前类的父亲列表
res = Demo.__base__  # 获取继承的第一个父类
print(res)

res = Demo.__bases__  # 获取当前类的父类列表
print(res)