'''
二、数组匹配
对于两个单调递增序列s1，s2，在其中可能存在这样的子序列ss1，ss2。对于任意i有（ss1[i+1]-ss1[i]）=（ss2[i+1]-ss2[i]），请找出这些子序列中元素个数最多的子序列。
子序列定义：对于长度为N的序列S，从其中删除n个（0<=n<=N）元素后就得到一个子序列SS

输入
两个单挑递增序列，单个元素取值范围-10^9 到 10^9，0<N<=10000

输出
如果能找到子序列，则第一行输出子序列长度，第二三行输出子序列
如果有多个满足条件的子序列，输出元素最小子序列
如果找不到子序列，输出0


'''
def compute(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * m for _ in range(n)]
    dp_list_s1 = [[[] for _ in range(m)] for _ in range(n)]
    dp_list_s2 = [[[] for _ in range(m)] for _ in range(n)]
    for i in range(m): dp[0][i] = 1
    for i in range(n): dp[i][0] = 1
    for i in range(m):
        dp_list_s1[0][i] = [s1[i]]
        dp_list_s2[0][i] = [s2[0]]
    for j in range(n):
        dp_list_s1[j][0] = [s1[0]]
        dp_list_s2[j][0] = [s2[j]]
    max_L = 0
    max_s1 = []
    max_s2 = []
    for i in range(1, m):
        for j in range(1, n):
            for k1 in range(1, i+1):
                for k2 in range(1, j+1):
                    if s1[i]-s1[i-k1] == s2[j]-s2[j-k2] and dp[j-k2][i-k1] != 0:
                        if dp[j-k2][i-k1] + 1 > dp[j][i]:
                            dp[j][i] = dp[j-k2][i-k1] + 1
                            dp_list_s1[j][i] = dp_list_s1[j-k2][i-k1] + [s1[i]]
                            dp_list_s2[j][i] = dp_list_s2[j-k2][i-k1] + [s2[j]]
            if dp[j][i] > max_L:
                max_L = dp[j][i]
                max_s1 = dp_list_s1[j][i]
                max_s2 = dp_list_s2[j][i]
    if max_L <= 1: 
        print('0')
    else: 
        print(max_L)
        print(' '.join(str(i) for i in max_s1))
        print(' '.join(str(i) for i in max_s2))

    return 

while(1):
    try:
        s1 = [int(i) for i in input().split()]
        s2 = [int(i) for i in input().split()]
        compute(s1, s2)
    except:
        break