# 编写一个程序，求100~999之间的所有水仙花数
# 如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。
# 153 = 1^3+5^3+3^3,因此153就是一个水仙花数


for i in range(100, 1000):
    if int(str(i)[0])**3 + int(str(i)[1])**3 + int(str(i)[2])**3 == i:
        print(i)


def sxh(n):
    if int(str(n)[0])**3 + int(str(n)[1])**3 + int(str(n)[2])**3 == n:
        return True
    else:
        return False


res = filter(sxh, range(100, 1000))
print(list(res))
