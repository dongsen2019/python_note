# calendar 日历模块

import calendar

# 返回指定年份和月份数据，月份的第一天是周几，和月份中的天数
# calendar.monthrange(年,月)
res = calendar.monthrange(2019, 12)
days = res[1]  # 当前月份的天数
w = res[0]+1  # 当前月份第一天

print("一 二 三  四 五 六 日")
d = 1
# for i in range(1, 35):
#     if d > res[1]:
#         break
#     elif i < res[0]:
#         print("  ", sep=' ', end=' ')
#     else:
#         print(f"{d:02d}", sep=' ', end=' ')
#         d += 1
#         if i % 7 == 0:
#             print()


while d < res[1]:
    for i in range(1, 8):
        if d > res[1] or (i < res[0]+1 and d == 1):
            print("  ", sep=' ', end=' ')
        else:
            print(f"{d:02d}", sep=' ', end=' ')
            d += 1
            if i % 7 == 0:
                print()

# print(res)
