'''
在一个地区有n个城市以及n-1条无向边，
每条边的时间边权都是1，并且这些城市是联通的，
即这个地区形成了一个树状结构。每个城市有一个等级。
现在小强想从一个城市走到另一个不同的城市，并且每条边经过至多一次，
同时他还有一个要求，起点和终点城市可以任意选择，但是等级必须是相同的。
但是小强不喜欢走特别远的道路，所以他想知道时间花费最小是多少。

示例1
输入
3
1 2 1
1 2
2 3
输出
2

https://www.nowcoder.com/questionTerminal/4b0fd3cd06dc4a899abf74996796f5c0

'''

import sys
def func(edge, rank):
    n = len(rank)
    def dfs(st, ed, count):
        if count > min0: return -1
        if st==ed: return count
        searched[st]=1
        for i in edge[st]:
            if searched[i]==0:
                t = dfs(i, ed, count+1)
                if t != -1:
                    return t
        searched[st]=0
        return -1

    rank_dict = {}
    for i in range(n):
        if rank[i] not in rank_dict:
            rank_dict[rank[i]]=[i]
        else:
            rank_dict[rank[i]].append(i)
    
    n2 = len(rank_dict)
    min0 = float('inf')
    if n2 == 0: return -1
    else:
        rank_keys = list(rank_dict.keys())
        for i in range(n2):
            candidates = rank_dict[rank_keys[i]]
            n3 = len(candidates)
            if n3>1:
                for j in range(n3):
                    for k in range(j+1, n3):
                        searched = [0]*n
                        t = dfs(candidates[j], candidates[k], 0)
                        if t != -1:
                            min0 = min(min0, t)
    if min0!=float('inf'): return min0
    else: return -1
            

n = int(sys.stdin.readline().strip())
rank = [int(i) for i in sys.stdin.readline().strip().split(' ')]
edges = [[] for _ in range(n)]
edge_count = [0]*n
for _ in range(n-1):
    a, b = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    edges[a-1].append(b-1)
    edges[b-1].append(a-1)
    edge_count[a-1]+=1
    edge_count[b-1]+=1

print(func(edges, rank, edge_count))
