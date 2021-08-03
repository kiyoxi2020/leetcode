'''
小强现在有n个节点,
他想请你帮他计算出有多少种不同的二叉树满足节点个数为n且树的高度不超过m的方案.
因为答案很大,所以答案需要模上1e9+7后输出.
树的高度: 定义为所有叶子到根路径上节点个数的最大值.
例如: 当n=3,m=3时,有5种方案

示例1
输入
3 3
输出
5
示例2
输入
3 2
输出
1
https://www.nowcoder.com/questionTerminal/aaefe5896cce4204b276e213e725f3ea

'''

import sys

n, m = map(int, sys.stdin.readline().strip().split(' '))

# dp[i][j]: the first i node, height j
dp = [[0] * (m+1) for _ in range(n+1)]
for j in range(1,m+1):
    dp[1][j] = 1
for i in range(2, n+1):
    for j in range(1,m+1):
        for k in range(0, i, 1):
            if i-k-1>=0 and i-k-1<=n and k>=0 and k<=n:
                if i-k-1==0: dp[i][j] += dp[k][j-1]
                elif k == 0: dp[i][j] += dp[i-k-1][j-1]
                else:
                    dp[i][j] += dp[i-k-1][j-1]*dp[k][j-1]

print((dp[-1][-1]%(10**9+7)))

