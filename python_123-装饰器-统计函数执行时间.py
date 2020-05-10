# lesson 123 统计函数执行时间
import time

# 定义一个统计函数执行时间的装饰器
def runtime(f):
    def inner():
        start = time.perf_counter()
        f()
        end = time.perf_counter()
        print(f"程序的执行时间位{end - start}秒")
    return inner


# 定义函数
@runtime
def func():
    for i in range(5):
        print(i, end=" ")
        time.sleep(1)

func()