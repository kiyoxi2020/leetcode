'''
小强发现当已知xy=B以及x+y=A时,
能很轻易的算出x^2+y^2的值.

但小强想请你在已知A和B的情况下,
计算出x^n+y^n的值.

因为这个结果可能很大,所以所有的运算都在模1e9+7下进行.

示例1
输入
3
4 4 3
2 3 4
5 2 6
输出
16
999999993
9009

https://www.nowcoder.com/questionTerminal/3b6dc1447d6d4ac4b9c2d45f1d4637ea

'''
import sys

mod0 = 10**9+7

def func2(a, b ,n):
    r0 = a
    r1 = (a*a%mod0 - 2*b%mod0+mod0)%mod0
    n-=2
    while(n):
        r2 = (a*r1%mod0-b*r0%mod0+mod0)%mod0
        r0=r1
        r1=r2
        n-=1
    return r1

T = sys.stdin.readline()
T = int(T.strip())
for _ in range(T):
    data = sys.stdin.readline().strip().split(' ')
    data = [int(i) for i in data]
    print(func2(data[0], data[1], data[2]))