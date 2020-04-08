# lesson 38
# 闭包函数
"""
1.在外函数中定义了局部变量，并且在内部函数中使用了这个局部变量
2.在外函数中返回了内函数，返回的内函数就是闭包函数
3.主要在于保护了外函数中的局部变量，既可以被使用，又不会被破坏
4.可以通过函数.__closure__查询是否是闭包函数，是返回cell，不是则返回None
"""

# 定义一个函数
def person():
    money = 0   # 函数中定义了一个局部变量
    # 工作 定义的内函数
    def work():
        nonlocal money # 在内函数中使用了外函数的临时变量
        money += 100
        print(money)
    # 在外函数中返回了内函数，这个内函数就是闭包函数
    return work


res = person()  # return work res = work
res()  # res() == work()
res()
res()
res()
print(res.__closure__)
print(person.__closure__)
# 此时 就不能够在全局中对money这个局部变量进行任何操作了
# 闭包的作用：保护了函数中的变量不受外部的影响，但是又不能不影响使用

