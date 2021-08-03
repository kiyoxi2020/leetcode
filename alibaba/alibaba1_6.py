'''
最近小强主办了一场国际交流会，大家在会上以一个圆桌围坐在一起。
由于大会的目的就是让不同国家的人感受一下不同的异域气息，
为了更好地达到这个目的，小强希望最大化邻座两人之间的差异程度和。
为此，他找到了你，希望你能给他安排一下座位，达到邻座之间的差异之和最大。

示例1
输入
4
3 6 2 9
输出
20
6 2 9 3

https://www.nowcoder.com/questionTerminal/afda747c4d0d414b839b7c37fc5e3baa
'''

import sys

n = int(sys.stdin.readline().strip())
data = [int(i) for i in sys.stdin.readline().strip().split(' ')]

data.sort()
st = 0
ed = n-1
out = []
sum0 = 0
while(st<ed):
    out.append(data[st])
    if len(out)>1:
        sum0+=abs(out[-2]-out[-1])
    out.append(data[ed])
    sum0+=abs(out[-2]-out[-1])
    st+=1
    ed-=1
if st==ed: 
    out.append(data[st])
    if len(out)>1:
        sum0+=abs(out[-2]-out[-1])
        sum0+=abs(out[-1]-out[0])
else:
    if len(out)>1:
        sum0+=abs(out[-1]-out[0])
print(sum0)
print(' '.join([str(i) for i in out]))



