'''
小强想要从[1,A] 中选出一个整数x,
从[1,B]中选出一个整数y.

使得满足 x/y = a/b 的同时且和的乘积最大。如果不存在这样的和,请输出“ 0 0”.

示例2
输入
1000 500 4 2
输出
1000 500

https://www.nowcoder.com/questionTerminal/669b796cf6074e1985eefe9b9b9cf103

'''

import sys

A, B, a, b = [int(i) for i in sys.stdin.readline().strip().split(' ')]

y = min(B, int(A*b/a))

def gcd(a, b):
    m, n = a, b
    while(n>0):
        m, n = n, m%n
    return m
    
if y>=1 and y>=b/a:
    if y*a%b == 0:
        print('%d %d'%(y*a/b, y))
    else:
        m = gcd(a, b)
        b0 = b//m
        y = y - y%b0
        print('%d %d'%(y*a/b, y))
        
else:
    print('0 0')

