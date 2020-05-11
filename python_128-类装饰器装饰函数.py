# lesson 128 类装饰器装饰函数

class Outer():
    # 魔术方法: 当把类的对象当作函数调用时，自动触发 obj()
    def __call__(self, func):
        self.func = func    # 把传进来的函数作为对象的成员方法
        return self.inner   # 返回一个函数

    # 再定义的需要返回的新方法中 去进行装饰和处理
    def inner(self, who):
        print("拿到妹子的微信。。。")
        self.func(who)
        print("看一场午夜电影")

@Outer()    # Outer() ==> obj() ==> obj(love) ==> __call__(love) ==> inner()
def love(who):
    print(f"{who}和妹子谈谈人生和理想。。。")

love("川哥") # inner("川哥")
print(love) # 此时的 love就是属于Outer类这个对象中的inner方法

