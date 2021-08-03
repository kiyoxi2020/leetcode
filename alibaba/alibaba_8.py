'''
有这样的一个方格游戏：这个游戏是这样的：

1.有n(m个方格，方格内每一个位置都有一个数，代表到达这个点后拥有的能量。

2.初始的时候在左上角，并将左上角的值作为初始能量，终点为右下角的点。

3.每一步只能往下或者往右走，且走一步需要消耗1点能量。不能在原地停留，即不会获得中间节点的能量并且能量不累计。

4.当你选择了一条可行的路径（这条路径消耗的能量不超过现有能量），你可以走到终点。

链接：https://www.nowcoder.com/questionTerminal/85e7e341dc764ae1866b9525c1937225
来源：牛客网

示例1
输入
2
3 3
2 1 1
1 1 1
1 1 1
6 6
4 5 6 6 4 3
2 2 3 1 7 2
1 1 4 6 2 7
5 8 4 3 9 5
7 6 6 2 1 5
3 1 1 3 7 2
输出
10
3948

https://www.nowcoder.com/questionTerminal/85e7e341dc764ae1866b9525c1937225
'''
import sys

def func(data):
    n, m = len(data), len(data[0])
    paths = [[0]*m for _ in range(n)]
    paths_sum = [[0]*m for _ in range(n)]
    for i in range(n-1,-1,-1):
        for j in range(m-1,-1,-1):
            if i==n-1 and j==m-1:
                paths[i][j] = 1
                paths_sum[i][j] = 1
            else:
                st1 = j+1
                ed1 = j+data[i][j]+1
                if st1<m and ed1 < m:
                    paths[i][j] += (paths_sum[i][st1]-paths_sum[i][ed1])
                elif st1<m:
                    paths[i][j] += paths_sum[i][st1]
                st1 = j
                for k in range(i+1, i+data[i][j]+1, 1):
                    if k<n:
                        ed1 -= 1
                        if ed1 < m:
                            paths[i][j] += (paths_sum[k][st1]-paths_sum[k][ed1])
                        else:
                            paths[i][j] += paths_sum[k][st1]
                if j+1<m:
                    paths_sum[i][j] = paths[i][j] + paths_sum[i][j+1]
                else:
                    paths_sum[i][j] = paths[i][j]
    return (paths[0][0])%10000
                


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    data = []
    for _ in range(n):
        t = [int(i) for i in sys.stdin.readline().strip().split(' ')]
        data.append(t)
    print(func(data))
