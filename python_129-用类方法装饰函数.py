# lesson 129 用类方法装饰函数

class Outer():
    def newinner(func):
        Outer.func = func   # 把传递进来的函数定义为类方法
        return Outer.inner  # 同时返回一个新的类方法

    def inner():
        print("拿到妹子微信")
        Outer.func()
        print("看一场午夜电影")

@Outer.newinner     # Outer.newinner(love) ==> Outer.inner
def love():
    print("和妹子谈谈人生喝喝茶。。。")

love()      # love() ==> Outer.inner()

"""
到目前为止以上所有形式的装饰器，包括 函数装饰器，类装饰器，类方法装饰器，都有一个共同特点：
都是在给函数去进行装饰，增加功能

还有一种装饰器，是专门装饰类的。也就是在类的定义的前面@装饰器这种语法
"""