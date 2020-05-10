# lesson 124 装饰器的嵌套

# 1.普通装饰器的定义

# 定义装饰器
# 外函数
def outer(func):
    # 内函数
    def inner():
        print("找到妹子，成功拿到微信。。。3")
        func()  # 在内函数中调用外函数中的形参-函数
        print("约妹子，看一场电影4")
    # 在外函数中返回内函数
    return inner

#使用一个装饰器

# @outer
# def love():
#     print("跟妹子畅谈人生和理想。。。")
#
# love() # 等价于调用 inner()

# 2.再定义一个装饰器
def kuozhan(f):
    def kzinner():
        print("扩展1")
        f()
        print("扩展2")
    return kzinner

# 装饰器的嵌套，自下而上
@kuozhan # 2.再使用上面的 kuozhan 装饰器，装饰 上一次返回的 inner 函数，又反悔了 kzinner 函数
@outer  # 1.先使用离得近的 outer装饰器 装饰love函数，返回了一个 inner函数
def love():
    print("跟妹子畅谈人生和理想。。。5")

love() # == inner()

