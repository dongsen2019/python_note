'''
100钱买100鸡
公鸡  3元
母鸡  1元
小鸡  0.5元
问：共有多少种方案
'''

x = 0   # 公鸡
y = 0   # 母鸡


for x in range(1, 34):
    for y in range(1, 101):
        z = 100 - x - y    # 小鸡
        if 3*x + y + 0.5*z == 100:
            print(x, y, z)

