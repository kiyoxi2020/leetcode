'''
小强作为强班的班长.决定带着包含他在内的个同学去春游.
路程走到一半,发现前面有一条河流.且只有一条小船.经过实验后发现,
这个小船一次最多只能运送两个人.而且过河的时间是等于两个人中体重较大的那个人的体重.
如果只有一个人,那么过河时间就是这个人的体重.现在小强想请你帮他分析如何安排才能在最短时间内使所有人都通过这条河流.
小强很懒,他并不想知道具体怎么过河,只要你告诉他最短的时间.

示例1
输入
2
4
2 10 12 11
4
2 3 7 8
输出
37
19

https://www.nowcoder.com/questionTerminal/ee3013ca07264e62801cc976bba05d1a
'''

import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    data = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    data.sort(key=lambda x: -x)
    data2 = []
    time = 0
    st = 0
    min1, min2 = data[-1], data[-2]
    while(st<n):
        if st==n-2:
            time += max(data[-1], data[-2])
            break
        elif st==n-3:
            time = time+data[st]+data[-1]+data[st+1]
            break
        else:
            max1, max2 = data[st], data[st+1]
            method1 = max1+min1+max2+min1
            method2 = min2+min1+max1+min2
            time+=min(method1, method2)
            st+=2
    print(time)
            

