'''
华为2021.7.21机考第一题

相当于求几段时间序列的最大交集
第一行输入N k，N表示有N个站点，k表示有k个乘客，其中N个站点分布在一个环上（注意是环，可以顺时针，可以逆时针），每个站点之间需要走5分钟
后面几行输入st id1 id2，其中st表示出发时间，id1表示出发站点，id2表示目的站点

求同一时间最多有多少个人在路上

------------
例1:
输入:
50 3
0 0 15
10 10 11
15 20 40
输出:
2
-----------
主要思路：首先整理出来每个人在路上的时间，然后求这些时间的最大交集，我采用的方法是对这些时间排序，然后依次求排序后相邻两点之间的中间点，
遍历这些中间点，求跟每段时间的交点个数，最后取最大即可，算法复杂度比较高，应该有更好的方法

'''
def func(N, k, matrix):
    time_range = []
    for st, id1, id2 in matrix:
        t1 = st
        id1, id2 = min(id1,id2), max(id1, id2)
        t2 = 5*min(id2-id1, id1+N-id2)
        time_range.append([t1,t2+t1])
    list0 = []
    for i in time_range:
        if i[0] not in list0: list0.append(i[0])
        if i[1] not in list0: list0.append(i[1])
    list0.sort()
    n = len(list0)
    out = []
    for i in range(n-1):
        t0 = (list0[i]+list0[i+1])/2.0
        count = 0
        for j in range(k):
            if t0<time_range[j][1] and t0>time_range[j][0]:
                count+=1
        out.append(count)
        
    
    return max(out)

import sys
while(1):
    data = sys.stdin.readline()
    if data=='': break
    data = data.strip().split(' ')
    N = int(data[0])
    k = int(data[1])
    matrix = []
    for i in range(k):
        data = sys.stdin.readline()
        data = data.strip().split(' ')
        if data[1]==data[2]: continue
        data = [int(j) for j in data]
        matrix.append(data)
    print(func(N, len(matrix), matrix))
        
            
