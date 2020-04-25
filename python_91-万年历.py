import time
import calendar
import os


def showdate(year, month):
    res = calendar.monthrange(year, month)
    w = res[0]+1
    days = res[1]
    print(f"======{year}年{month}月======")
    print('*'*21)
    print("一 二 三  四 五 六 日")
    d = 1
    while d < days:
        for i in range(1, 8):
            if d > res[1] or (i < w and d == 1):
                print("  ", sep=' ', end=' ')
            else:
                print(f"{d:02d}", sep=' ', end=' ')
                d += 1
                if i % 7 == 0:
                    print()
    print()
    print('*' * 21)


timetup = time.localtime()
year = timetup.tm_year
month = timetup.tm_mon

while True:
    showdate(year, month)
    print("< 上个月   下个月 >")
    c = input("请输入您的选择：")
    if c == '<':
        if month == 1:
            year -= 1
            month = 12
        else:
            month -= 1
    elif c == '>':
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1
    else:
        print("输入错误，请重新输入：")

os.system("cls")
