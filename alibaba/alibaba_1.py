'''
小强现在有个n物品,每个物品有两种属性x_i和y_i
他想要从中挑出尽可能多的物品满足以下条件:
    对于任意两个物品i和j,满足x_i<x_j且y_i<y_j 或者 x_i>x_j且y_i>y_j.
    问最多能挑出多少物品.

输入
2
3
1 3 2
0 2 3
4
1 5 4 2 
10 32 19 21
输出
2
3

https://www.nowcoder.com/questionTerminal/a55198d2e65746009110226f2f6c8533

'''

import sys
from bisect import bisect_left
def func2(out, v):
    st = 0
    ed = len(out)
    pos = -1
    while(st<=ed):
        mid = (st+ed)//2
        if out[mid] < v:
            pos = mid
            st = mid+1
        else:
            ed = mid-1
    pos = min(pos+1, len(out)-1)
    if out[pos]>v:
        out[pos] = v
    return

def func(x, y):
    n = len(x)
    data = sorted(zip(x,y), key=lambda x: (x[0],-x[1]))
    #data.sort(key=lambda x: -x[1])
    #data.sort(key=lambda x: x[0])
    dp = []
    dp.append(data[0][1])
    for i in range(1, n):
        if data[i][1] > dp[-1]:
            dp.append(data[i][1])
        else:
            st = 0
            ed = len(dp)-1
            func2(dp,data[i][1])
            #idx = bisect_left(dp, data[i][1])
            #dp[idx]=data[i][1]
    return len(dp)

T = sys.stdin.readline()
T = int(T.strip())
for _ in range(T):
    n = sys.stdin.readline()
    n = int(n.strip())
    x = sys.stdin.readline()
    x = x.strip().split(' ')
    x = [int(i) for i in x]
    y = sys.stdin.readline()
    y = y.strip().split(' ')
    y = [int(i) for i in y]
    print(func(x, y))
    