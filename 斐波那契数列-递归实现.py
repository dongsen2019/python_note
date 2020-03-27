def Fibonacci(a):
    if a == 1:
        return 0
    elif a == 2:
        return 1
    else:
        return Fibonacci(a-1) + Fibonacci(a-2)


n = int(input("请输入求得的项数:"))
print(Fibonacci(n))


