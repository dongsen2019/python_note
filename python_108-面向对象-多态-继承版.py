# lesson 107  多态-派生类重载父类方法


"""
定义一个结构规范类，其他类都是继承这个类，并实现(重写)父类中的方法
由于每个对象实现父类的方法或者过程都不相同，最后的结果是不一样的形态
"""

# 定义 USB
class USB():
    """
     接口规范类，需要子类继承并实现start()方法
     规范类的方法不做任何实现功能
    """
    # 在usb类中定义一个规范的接口方法，但是不实现任何功能
    def start(self):
        pass


# 定义鼠标类
class Mouse():
    def start(self):
        print("鼠标启动成功，可以双击单击嗨起来。。。")


# 定义键盘类
class KeyBord():
    def start(self):
        print("键盘启动成功，赶紧双击666。。。")


# 定义 U盘 类
class Udisk():
    def start(self):
        print("U盘启动了，赶紧检查一下我的种子还在不在。。。")


# 实例化对象
m = Mouse()  # 鼠标对象
k = KeyBord()  # 键盘对象
u = Udisk()  # U盘对象

m.start()
k.start()
u.start()
