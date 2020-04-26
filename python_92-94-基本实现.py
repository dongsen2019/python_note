# lesson 94 基本实现

"""
类名的书写规范，建议使用驼峰命名法
    大驼峰：MyCar XiaoMi
    小驼峰：myCar xiaoMi

一个类有特征和功能两个内容组成：
    属性：就是一个描述：白色，品牌：奥迪，排量：2.4 ......
    方法：就是一个能力：端茶，倒水，做饭
"""

# 定义一个汽车的类
class Cart():
    # 属性 ==> 特征 ==> 变量
    color = "白色"    # 表示颜色属性
    brand = "奥迪"    # 表示品牌属性
    pailiang = 2.4   # 表示排列属性

    # 方法 ==> 功能 ==> 函数
    def luohuo(self):
        print("小汽车能拉货")

    def doufeng(self):
        print("小汽车能兜风")

    def bamei(self):
        print("把妹子去嗨。。。")

# 如何去使用这个类
# 通过类实例化一个对象

aodi = Cart()

# print(aodi, type(aodi))
# <__main__.Cart object at 0x0000000002996A58> <class '__main__.Cart'>

# 调用对象的方法
aodi.bamei()

# 获取对象的属性
print(aodi.brand)