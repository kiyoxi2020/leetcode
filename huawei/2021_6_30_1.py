'''
一、路线规划
某公司有M个园区，从0到M-1编号，已知2个园区的距离，描述如下：0 1 3，表示从0号园区到1号园区的距离是3（1到0号园区也是3），已知N段距离，未给出距离的则为不可达，现在有一个员工想从A区出发，走遍所有的园区，同一园区只能够经过一次，请计算该员工的最短距离。

输入
第一行：园区个数M，起始园区编号，已知距离个数N
第二行到N行：第一个数字为起始园区，第二个数字为目的园区，第三个数字为距离，中间使用空格区分。
约束：

0<M<=15，0<N<=45
所有输入数据>=0，距离输入都为有效范围，不用考虑无效输入。距离范围为：[1,1000]
每个园区路径不超过3条
输出
最短距离，如无法完成题目条件，则输出-1

'''

def compute(dis, M, st):
    dp = [[float('inf')] * (M) for _ in range(M)]
    dp_searched = [[[] for _ in range(M)] for _ in range(M)]
    dp[0][st] = 0
    dp_searched[0][st] = [st]

    for i in range(1, M, 1):
        for j in range(M):
            if dp[i-1][j] != float('inf'):
                for k in range(M):
                    if dis[j][k] != float('inf') and k not in dp_searched[i-1][j]:
                        if dp[i-1][j]+dis[j][k] < dp[i][k]:
                            dp_searched[i][k] = dp_searched[i-1][j] + [k]
                            dp[i][k] = dp[i-1][j]+dis[j][k]

    out = min([i for i in dp[M-1]]) 
    return out if out != float('inf') else -1


while(1):
    try:
        M, st, N = [int(i) for i in input().split(' ')]
        dis = [[float('inf')] * M for _ in range(M)]
        for i in range(N):
            i, j, d = [int(i) for i in input().split(' ')]
            dis[i][j] = d
            dis[j][i] = d
        out = compute(dis, M, st)
        print(out)
    except: break