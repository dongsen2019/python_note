# lesson 60
from functools import reduce
dic1 = {'user': 'admin', 'age': 20, 'phone': '133'}
print([(i, dic1[i]) for i in dic1])
lst = [str(i)+'='+str(dic1[i]) for i in dic1]
res = reduce(lambda x, y: x+'&'+y, lst)
print(res)  # user=admin&age=20&phone=133


# 案例2 用列表推导式把列表中的字符转化为小写
# ["AAAAA", 'bbBbB','CCCcc']
lst = ["AAAAA", 'bbBbB', 'CCCcc']
print([i.lower() for i in lst])


# 案例3 x 是0-5之间的奇数，y是0-5之间的偶数， 把x, y组成一个元组，放到列表中
print([(x,y) for x in range(1,6,2) for y in range(0,6,2)])

# 案例4 用列表推导式 完成 九九乘法表
print([f'{i}*{j}={i*j}' for i in range(1, 10) for j in range(1, i+1)])

# 案例5
M = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

N = [
    [2, 2, 2],
    [3, 3, 3],
    [4, 4, 4]
]

print(len(M))

res = [[M[i][j]*N[i][j] for j in range(0, len(M[0]))] for i in range(0,len(M))]
print(res)
