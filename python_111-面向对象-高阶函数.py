# lesson 111 面向对象的高阶函数

class A():
    pass


class B(A):
    pass


class C(A):
    ccc = None
    pass


class D(B, C):
    name = 'a'
    age = 20
    pass

c = C()

# issubclass(子类，父类) # 检测一个类是否为另一个类的子类
# res = issubclass(D,B)

# isinstance(对象，类) # 检测一个对象是否是指定类或该类基类的实例化
"""
当检测对象是否会基类的实例化时，也返回True
"""
res = isinstance(c, D)

# hasattr(对象/类，"成员名称") 检测类/对象是否包含指定名称的成员
"""
由于私有属性，解释器对其进行重命名，所有检测为True
"""
res = hasattr(c, "ccc")

# getattr() # 获取类/对象的成员
res = getattr(D, "name")  # a

# setattr(对象/类，"成员名称"，"成员的值") 设置类/对象的成员的属性
setattr(c, "sanwei", 30)

# delattr(对象/类，"成员名称") 删除类/对象的成员属性和del直接删除的结果是一样的
# delattr(c, "sanwei")
# print(c.sanwei)

# dir() # 获取当前对象所以可以访问的成员的列表
res = dir(c)
print(res)

