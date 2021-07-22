'''
华为2021.7.21机考第二题
一个机器作业分配问题
第一行输入N k，其中N表示有几个机器，k表示有几个任务
后面几行输入t r，其中t表示每个任务耗费时间，r表示任务的优先级，越小优先级越高

求最短的作业时间

------------
例1:
输入:
2 2
3 1
4 2
输出:
4
------------
主要思路：设立cost=[0]*N变量，表示每个机器的工作时常，
对任务按照优先级从1到高排序，然后首先取出优先级高的任务，按照耗费时间由高到低排序，
依次找cost中最小的变量，将耗费时间加上去
遍历完所有任务，取cost的最大值即可

'''

def func(N, k, data):
    cost = [0]*N
    data.sort(key=lambda x: x[1])
    i = 0
    while(1):
        if i == k: break
        t = data[i][1]
        data0 = []
        while(i<k and data[i][1]==t):
            data0.append(data[i])
            i+=1
        data0.sort(key=lambda x:-x[0])
        for tt in data0:
            cost.sort()
            cost[0]+=tt[0]
    return max(cost)

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
        matrix.append([int(i) for i in data])
    print(func(N, k , matrix))
        
        
            
        
        
        
        
    