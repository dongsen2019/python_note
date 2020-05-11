# lesson 127 带有参数的装饰器

# 如果你的装饰器需要有参数，那么给当前的装饰器套一个壳，用于接收装饰器的参数
def kuozhan(var):
    def outer(func):
        def inner1(who):
            print("妹子给了你微信")
            func(who)
        def inner2(who):
            print("妹子给介绍了大妈")
            func(who)

        # 装饰器壳的参数，可以用于在函数内去做流程控制
        if var == "高富帅":
            return inner1
        else:
            return inner2

    return outer


@kuozhan("高富帅")     # kuozhan(var) ==> outer() ==> outer(love) ==> inner()
def love(who):
    print("谈谈人生。。。",who)

love("dongsen")