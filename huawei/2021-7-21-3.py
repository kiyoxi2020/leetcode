'''
华为2021.7.21机考第三题

一个有向无环的连通图，每条边上有负载值，求负载值和最大的通路
输入[st,ed,c]，表示存在从节点st到节点ed的边，边上的负载为c
输出目标为负载最大通路对应的负载值之和

------------
例1:
输入:
[[1,2,5],[1,3,5],[4,2,10],[2,5,5],[3,4,10],[3,7,10],[4,7,5],[5,6,5],[6,7,5]]
输出：
40
------------
基本思路：找到入度为0的节点，从该节点开始dfs，直到无法再前进，此时记录负载值，回溯，继续遍历下一个节点
返回负载的最大值即可

'''

def func(matrix):
    n = len(matrix)
    st = 0
    while(st<n):
        if sum([matrix[i][st] for i in range(n)]) == 0:
            break
        st+=1
    searched = [0]*n 
    out = [0]
    def dfs(ind, n, cost):
        flag = 0
        for i in range(n):
            if i != ind and searched[i]==0 and matrix[ind][i]>0:
                flag = 1
                searched[i] = 1
                dfs(i, n, cost+matrix[ind][i])
                searched[i] = 0
        if flag == 0: out.append(cost)
        return
    searched[st] = 1
    dfs(st, n, 0)
    return max(out)

import sys
while(1):
    data = sys.stdin.readline()
    if data == '': break
    data = data.strip()
    data = data.split(',')
    out = []
    for i in data:
        if '[' not in i and ']' not in i: out.append(int(i))
        else:
            if '[' in i:
                i = i.split('[')
                out.append(int(i[-1]))
            else:
                i = i.split(']')
                out.append(int(i[0]))
    n = len(out)
    st_list = {}
    for i in range(0,n,3):
        st = out[i]
        if st not in st_list:
            st_list[st]=len(st_list)
        ed = out[i+1]
        if ed not in st_list:
            st_list[ed]=len(st_list)
    N = len(st_list)
    matrix = [[0] * N for _ in range(N)]
    for i in range(0,n,3):
        st = out[i]
        ed = out[i+1]
        c = out[i+2]
        matrix[st_list[st]][st_list[ed]] = c
    print(func(matrix))
        

    
    
                