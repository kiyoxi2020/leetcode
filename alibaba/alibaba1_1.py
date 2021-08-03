'''
链接：https://www.nowcoder.com/questionTerminal/f5a3b5ab02ed4202a8b54dfb76ad035e
来源：牛客网

有n个物品，每个物品有k个属性，第i件物品的第j个属性用一个正整数表示记为a_{i,j}
​
两个不同的物品i,j被称为是完美对的当且仅当a_{i,1}+a_{j,1} = a_{i,2}+a_{j,2}=\dots=a_{i,k}+a_{j,k}a 
求完美对的个数。

输出描述:
一行一个数字表示答案
示例1
输入
5 3
2 11 21
19 10 1
20 11 1
6 15 24
18 27 36
输出
3

'''

import sys

n, k = [int(i) for i in sys.stdin.readline().strip().split(' ')]
count = 0
dict = {}
i = 0
while(i<n):
    data = [int(j) for j in sys.stdin.readline().strip().split(' ')]
    delta1 = ''
    delta2 = ''
    for j in range(1,k,1):
        delta1 += str(data[j]-data[j-1])
        delta2 += str(-data[j]+data[j-1])
    if delta2 in dict : count+=dict[delta2]
    if delta1 not in dict: dict[delta1] = 1
    else: dict[delta1] += 1
    i+=1

print(count)