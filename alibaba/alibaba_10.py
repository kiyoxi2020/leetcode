'''
小强有两个序列a和b，这两个序列都是由相同的无重复数字集合组成的，
现在小强想把a序列变成b序列，他只能进行以下的操作：
    从序列a中选择第一个或者最后一个数字并把它插入a中的任意位置。

问小强至少需要几次操作可以将序列a变为序列b。

示例1
输入
4
4 2 3 1
1 2 3 4
输出
2

https://www.nowcoder.com/questionTerminal/b65b8b1376d94d4b8d4718ba2f4c0022

'''

import sys

def func(a, b, n):
    dict = {}
    count = 1
    for i in b:
        dict[i] = count
        count += 1
    i = 0
    while(i<n):
        a[i] = dict[a[i]]
        i+=1
    count = 1
    max_count = 0
    for i in range(1, n):
        if a[i]>a[i-1]:
            count+=1
        else:
            max_count = max(max_count, count)
            count = 1
    
    return n-max_count


        
n = int(sys.stdin.readline().strip())
a = [int(i) for i in sys.stdin.readline().strip().split(' ')]
b = [int(i) for i in sys.stdin.readline().strip().split(' ')]
print(func(a, b, n))
