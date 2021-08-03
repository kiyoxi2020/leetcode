'''
有个牛牛一起去朋友家吃糖果，第i个牛牛一定要吃ai块糖果.

而朋友家一共只有m块糖果，可能不会满足所有的牛牛都吃上糖果。

同时牛牛们有k个约定，
每一个约定为一个牛牛的编号对(i,j)，
表示第i个和第j个牛牛是好朋友，他俩要么一起都吃到糖果，要么一起都不吃。

保证每个牛牛最多只出现在一个编号对中。

您可以安排让一些牛牛吃糖果，一些牛牛不吃。

要求使能吃上糖果的牛牛数量最多（吃掉的糖果总量要小于等于m），并要满足不违反牛牛们的k个约定。

示例1
输入
3 10
5 1 5
1
1 3
输出
2

https://www.nowcoder.com/questionTerminal/e7a006abf5ec412a939f0d33725f06ed

'''
import sys

def read():
    return sys.stdin.readline().strip().split(' ')

def func(a1, a2, m):
    count = 0
    a1.sort()
    a2.sort()
    n1,n2 = len(a1), len(a2)
    st1, st2 = 0, 0
    while((st1<n1 or st2<n2) and m>0):
        if (st2<n2 and a2[st2]>m) and (st1<n1 and a1[st1]>m):
            break
        if st1<=n1-2 and st2<=n2-1:
            t1 = a1[st1]+a1[st1+1]
            t2 = a2[st2]
            if t1<t2 and t1<=m:
                m-=t1
                st1+=2
                count+=2
            elif t1>=t2 and t2<=m:
                m-=t2
                st2+=1
                count+=2
            elif a1[st1]<=m:
                m-=a1[st1]
                st1+=1
                count+=1
            else:
                break
        else:
            if st2<=n2-1:
                if a2[st2]<=m:
                    m-=a2[st2]
                    st2+=1
                    count+=2
            if st1<=n1-1:
                if a1[st1]<=m:
                    m-=a1[st1]
                    st1+=1
                    count+=1

    return count

n, m = [int(i) for i in read()]
a = [int(i) for i in read()]
k = int(sys.stdin.readline().strip())
searched = [0] * n
a_new1 = []
a_new2 = []
for _ in range(k):
    t = [int(i) for i in read()]
    a_new2.append(a[t[0]-1]+a[t[1]-1])
    searched[t[0]-1]=1
    searched[t[1]-1]=1
for i in range(n):
    if searched[i] == 0:
        a_new1.append(a[i])
print(func(a_new1, a_new2, m))


