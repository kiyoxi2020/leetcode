'''
小强今天体检，其中有一个环节是测视力
小强看到的视力表是一张N*N的表格，
但是由于小强视力太差，他无法看清表格中的符号。
不过热爱数学的他给自己出了这样一个问题：
    假设现在有a个向上的符号，b个向下的符号，c个向左的符号，d个向右的符号，
    把这些符号填到视力表中，总共有多少种可能的情况呢？


输入描述:
第一行输入五个数N, a, b, c, d
输出描述:
输出一个数字，表示答案
由于结果可能很大，只需输出对998244353取模之后的结果即可

示例1
输入
2 3 1 0 0
输出
4


https://www.nowcoder.com/questionTerminal/83ad5dde4e284883bef77013fc3c50fd

'''


import sys
mod0 = 998244353

N, a, b, c, d = [int(i) for i in sys.stdin.readline().strip().split(' ')]



def func(n, k):
    i = n
    out = 1
    while(i>=n-k+1):
        out *= i
        i-=1
    i = 1
    while(i<=k):
        out /= i
        i+=1
    return int(out)


out = func(N*N, a) * func(N*N-a, b) * func(N*N-a-b, c)
print(out%mod0)
