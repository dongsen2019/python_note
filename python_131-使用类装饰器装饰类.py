# lesson 131 使用类装饰器装饰类

class KuoZhan():
    def __call__(self, cls):
        # 把接收的类，赋值给当前对象，作为一个属性
        self.cls = cls
        # 返回一个函数
        return self.newfunc

    def newfunc(self):
        self.cls.name = "我是在类装饰器中追加的新属性 name"
        self.cls.func2 = self.func2
        # 返回传递进来的类的实例化结果，obj
        return self.cls()

    def func2(self):
        print("我是在类装饰器中追加的新方法")

@KuoZhan()  # KuoZhan() ==> obj() ==> obj(Demo) ==> __call__() ==>newfunc
class Demo():
    def func(self):
        print("我是Demo类中定义的func方法")

obj = Demo()  # Demo() ==> 调用newfunc() ==> return 实例化cls(Demo)的对象obj
obj.func()
obj.func2()
print(obj.name)

print(obj)

