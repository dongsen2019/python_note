# lesson 126   装饰器带有参数的函数

# 定义装饰器
def outer(func):
    # 如果装饰带有参数的函数，需要在内函数中定义形参，并传递给调用的函数。
    # 因为调用原函数等于调用内函数
    def inner(var):
        print("找到妹子，成功拿到微信。。")
        func(var)
        print("约妹子，看一场午夜电影。。")
    return inner

# 有参数的函数
@outer
def love(name):
    print(f"跟{name}妹子畅谈人生。。。")

love("思思")  # love() ==> inner()    love("思思") ==> inner("思思")




