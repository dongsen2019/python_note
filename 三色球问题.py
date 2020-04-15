# 三色球问题

"""
有红、黄、蓝三种颜色的球，其中红球三个，黄球三个，绿球6个。
先将这12个球混合放在一个盒子中，从中任意摸出8个球，编程计算摸出球的各种颜色搭配。
"""

lst = []
for i in range(0, 4):
    for j in range(0, 4):
        for k in range(2, 7):
            if i+j+k == 8:
                lst.append((i, j, k))
print(lst)



