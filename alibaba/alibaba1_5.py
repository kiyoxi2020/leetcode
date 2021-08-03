'''
在一张2D地图上小强有n座房子,
因为地理位置的原因没有办法给每座房子提供水源,
所以小强打算修建一条平行y轴的水渠.因为这条水渠无限长.
所以能够看做是一条平行于y轴的直线. 

现在小强想确定修建水渠的位置,能够使得这n座房子到水渠的垂直距离和最小,
请你输出最小的距离和.

示例1
输入
4
0 0
0 50
50 50
50 0
输出
100

https://www.nowcoder.com/questionTerminal/ca184e56353b4a9db1872af554694013

'''

import sys

n = int(sys.stdin.readline().strip())
y = []
j = 0
while(j<n):
    a, b = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    y.append(a)
    j+=1
y.sort()
b_center = y[n//2]
out = sum([abs(i-b_center) for i in y])
print('%d'%out)