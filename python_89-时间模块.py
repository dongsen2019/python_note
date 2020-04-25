# 内置模块-时间模块-time

import time

"""
概念：
    1.时间戳：表示从1970年1月1日0时0分0秒到现在的经过秒数，目前可以计算到2038年  例如：1587802817.4335792
    2.时间字符串：Sat Apr 25 18:26:03 2020
    3.时间元组：time.struct_time(tm_year=2020, tm_mon=4, tm_mday=25, tm_hour=18, tm_min=26, tm_sec=26, tm_wday=5, tm_yday=116, tm_isdst=0)
"""

# 1.获取当前系统的时间戳
# res = time.time()  # 1587802817.4335792

# 2.获取当前系统时间，时间字符串
# res = time.ctime()  # Sat Apr 25 18:26:03 2020

# 3.获取当前系统时间，时间元组
res = time.localtime()
# time.struct_time(tm_year=2020, tm_mon=4, tm_mday=25, tm_hour=18, tm_min=26, tm_sec=26,tm_wday=5, tm_yday=116, tm_isdst=0)

# 4.以上时间字符串和时间元组可以通过制定的时间戳来获取
t = 1587801800.4335792
res = time.ctime(t)  # Sat Apr 25 16:20:17 2020
res = time.localtime(t)  # time.struct_time(tm_year=2020, tm_mon=4, tm_mday=25, tm_hour=16, tm_min=20, tm_sec=17, tm_wday=5, tm_yday=116, tm_isdst=0)

# 5.使用localtime方法获取的时间元组，如何格式化成为 xxxx年xx月xx日 时：分：秒 星期几
print(f"{res.tm_year}年{res.tm_mon}月{res.tm_mday}日 {res.tm_hour}:{res.tm_min:02d}:{res.tm_sec} 星期{res.tm_wday+1}")
"""
该语法在大多数情况下与旧式的 % 格式化类似，只是增加了 {} 和 : 来取代 %。 例如，，'%03.2f' 可以被改写为 '{:03.2f}'。
"""

# 6.strftime() 格式化时间  年-月-日  时：分：秒  星期几
res = time.strftime("%Y-%m-%d %H:%M:%S %w")

# 7.sleep(sec) 在给定的秒数内暂停调用线程的执行。该参数可以是浮点数，以指示更精确的睡眠时间
# time.sleep(5)

# 8.100万次的数字比较，需要的执行时间
s = time.perf_counter()
for i in range(1000000):
    if 3 == 4:
        pass
e = time.perf_counter()

# 9.strptime()
# time.strptime("30 Nov 00", "%d %b %y")
# 输出 time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
#                  tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

print(res)

