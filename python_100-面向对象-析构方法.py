# 析构方法 __del__

"""
定义一个类，完成一个日志的纪录
    调用这个对象的时候，传递一个日志信息
    这个对象创建一个文件，开始写入，并在最后关闭这个文件
"""

import time

class writeLog():
    # 成员属性

    fileurl = './'  # 文件的路径
    filename = "2019-09-19"  # 日志文件的名称
    fileobj = None # 文件对象

    # 成员方法

    def __init__(self):
        # 完成文件的打开
        print("对象被创建，初始化")
        self.fileobj = open(self.fileurl+self.filename, 'a+', encoding='utf-8')

    def log(self, s):
        print(f"把日志内容:{s}写入文件中")

    # 析构方法
    def __del__(self):
        print('析构方法触发了')
        # 在对象被销毁时，关闭在初始化方法中打开的文件对象
        self.fileobj.close()


wl = writeLog()
wl.log('str')

"""
__del__
    析构方法会在对象被销毁时自动触发
    作用：关闭一些开发的资源
    注意：是对象被销毁时触发了这个方法，而不是这个方法销毁了对象

对象会在哪些情况下被销毁？
    1.当对象对其作用的域完毕时
    2.使用 del 删除时
    3.临时对象
"""

# 使用手动删除对象
del wl

# 临时对象
writeLog()

print("......")

# 最后思考一个问题？
class Cart():
    brand = ''
    def __init__(self,b):
        self.brand = b
        print(f"初始化方法被触发：创建{self.brand}汽车")

    def __del__(self):
        print(f"析构方法被触发：{self.brand}汽车已经被销毁")


# 问题1 下列程序中对象的销毁顺序
# bm = Cart('宝马')
# bc = Cart('奔驰')
# fll = Cart('法拉利')

"""
初始化方法被处罚：创建宝马汽车
初始化方法被处罚：创建奔驰汽车
初始化方法被处罚：创建法拉利汽车
析构方法被处罚：宝马汽车已经被销毁
析构方法被处罚：奔驰汽车已经被销毁
析构方法被处罚：法拉利汽车已经被销毁
"""


# 问题2 ''
Cart('宝马')
Cart('奔驰')
Cart('法拉利')

"""
初始化方法被触发：创建宝马汽车
析构方法被触发：宝马汽车已经被销毁
初始化方法被触发：创建奔驰汽车
析构方法被触发：奔驰汽车已经被销毁
初始化方法被触发：创建法拉利汽车
析构方法被触发：法拉利汽车已经被销毁
"""