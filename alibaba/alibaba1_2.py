'''
有n个物品可供选择，必须选择其中m个物品，请按字典序顺序输出所有选取方案的物品编号

123与312与321等被认为是同一种方案，输出字典序最小的即可

示例1
输入
4 1
输出
1
2
3
4

https://www.nowcoder.com/questionTerminal/d03abbd6587d4951a9d2d872e310a3f3

'''
import sys

def func(n, m):
    data = [i+1 for i in range(n)]
    out = []
    def dfs(st, list0):
        if len(list0) == m:
            out.append(' '.join([str(i) for i in list0]))
            return
        for i in range(st+1, n):
            list0.append(data[i])
            dfs(i, list0)
            list0.pop(-1)
        return
    
    for i in range(n):
        dfs(i, [data[i]])
    for i in out:
        print(i)
    return

n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
func(n, m)