'''
小强有一个长度为n的数组a和正整数m.
他想请你帮他计算数组a中有多少个连续子区间[l,r],其区间内存在某个元素出现的次数不小于m次?
例如数组a=[1,2,1,2,3]且m=2,
那么区间[1,3],[1,4],[1,5],[2,4],[2,5]都是满足条件的区间,但区间[3,4]等都是不满足条件的.

示例1
输入
5 2
1 2 1 2 3
输出
5

https://www.nowcoder.com/questionTerminal/778ae1581eb54959bce91afe0b51c3ff
'''
import sys

def func2(data, m):
    n = len(data)
    dict = {}
    st = 0
    count = 0
    dict[data[st]]=1
    for i in range(n):
        if st<n and dict[data[st]]<m:
            while(st < n and dict[data[st]]<m):
                st+=1
                if st>=n: break
                if data[st] not in dict: dict[data[st]]=0
                dict[data[st]]+=1
        count += (n-st)
        dict[data[i]]-=1
    return count


def func(data, m):
    n = len(data)
    satisfied = [0]*n
    dict = {}
    count = 0
    for i in range(n):
        if data[i] in dict:
            if len(dict[data[i]])>=m-1:
                st = dict[data[i]][-m+1]
                count += ((n-i) * (st+1-sum(satisfied[:st+1])))
                satisfied[dict[data[i]][-m+1]] = 1
            dict[data[i]].append(i)
        else:
            dict[data[i]] = [i]
    return count

n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
data = [int(i) for i in sys.stdin.readline().strip().split(' ')]
print(func2(data, m))
