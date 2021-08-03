'''
小强有一个3*n的矩阵a，
他将a中每列的三个数字中取出一个按顺序组成一个长度为n的数组b，
即b_i可以是a_1i, a_2i, a_3i其中任意一个。
问\sum(|b_i-b_{i+1}|)的最小值是多少。

示例1
输入
5
5 9 5 4 4
4 7 4 10 3
2 10 9 2 3
输出
5

https://www.nowcoder.com/questionTerminal/a132e8338b9e4545a154b1407cd41fd2

'''

import sys

n = int(sys.stdin.readline().strip())
data = []
for _ in range(3):
    data.append([int(i) for i in sys.stdin.readline().strip().split(' ')])
last = [0]*3
i = 1
while(i<n):
    last1 = [0]*3
    for j in range(3):
        last1[j] = min([abs(data[k][i-1]-data[j][i])+last[k] for k in range(3)])
    last = last1
    i+=1
print(min(last))
