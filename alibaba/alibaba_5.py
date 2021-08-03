'''
最近部门要选两个员工去参加一个需要合作的知识竞赛，
每个员工均有一个推理能力值Ai，以及一个阅读能力值Bi。
如果选择第i个人和第j个人去参加竞赛，
那么他们在阅读方面所表现出的能力为X=(Bi+Bj)/2，
他们在推理方面所表现出的能力为Y=(Ai+Aj)/2。
现在需要最大化他们表现较差一方面的能力，
即让min(X, Y)尽可能大，问这个值最大是多少。

示例1
输入
3
2 2
3 1
1 3
输出
2.0

https://www.nowcoder.com/questionTerminal/2a9089ea7e5b474fa8f688eae76bc050

'''
import sys

def func(data):
    n = len(data)
    data.sort(key=lambda x: abs(x[0]-x[1]))
    maxa, maxb = data[0][0], data[0][1]
    max0 = 0
    for i in range(n):
        a1, b1 = data[i]
        if b1<a1: max0 = max((b1+maxb)/2., max0)
        else: max0 = max((a1+maxa)/2., max0)
        maxa = max(maxa, a1)
        maxb = max(maxb, b1)
    return max0

n = int(sys.stdin.readline().strip())
data = []
for _ in range(n):
    t = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    data.append(t)
print(func(data))
