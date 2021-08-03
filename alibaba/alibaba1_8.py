
'''
很久很久以前，在蚂蚁森林里住着n只小动物，编号从1到n。
编号越小的动物能力值越大。现在他们想投票选出一只小动物当森林之王，
对于每只小动物来说，如果他有崇拜的对象，
那么他可能投票选择自己，或与自己崇拜的对象投相同票；
如果他没有崇拜的对象，那么他投票只可能选择自己。
每只小动物只会崇拜能力值比自己大的小动物。

记者小强拜访了这n只小动物，了解到每只小动物是否有崇拜的对象以及具体是谁。现在他想知道每个人能得到的最高票数是多少。
示例1
输入
4
0 1 1 1
输出
4
1
1
1


https://www.nowcoder.com/questionTerminal/276be492542443139857d02198817c3e

'''
import sys

n = int(sys.stdin.readline().strip())
data = [int(i) for i in sys.stdin.readline().strip().split(' ')]

out = [0] * n
for i in range(n-1, -1, -1):
    out[i] += 1
    if data[i] != 0:
        out[data[i]-1] += out[i]
    
for i in out:
    print(i)

