n1 = 0
n2 = 1
count = 2
n = int(input("第几项："))

if n == 1:
    print(0)
elif n == 2:
    print(1)
else:
    pre = n1
    cur = n2
    while count < n:
        temp = cur + pre
        pre, cur = cur, temp
        count += 1
    print(cur)




