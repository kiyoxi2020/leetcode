'''
有一个长度为n的字符串s，
你可以删除其中的m个字符，
使剩余字符串的字典序最小，
输出这个剩余字符串。

示例1
输入
2
5 2
abcab
10 4
lkqijxsnny
输出
aab
ijsnny

https://www.nowcoder.com/questionTerminal/8951775b97d949628675398b6639d79c

'''

import sys

T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = [int(i) for i in sys.stdin.readline().strip().split(' ')]
    data = sys.stdin.readline().strip()
    count = 0
    out = [data[0]]
    i = 1
    while(i<n):
        while(len(out)>0 and data[i]<out[-1]):
            out.pop(-1)
            count+=1
            if count == m:
                break
        out.append(data[i])
        if count == m:
            break
        i+=1
    if count == m:
        out0 = ''.join(out) 
        if i+1<n:
            out0 += data[i+1:]
    else:
        out0 = ''.join(out)
        out0 = out0[:len(out0)-(m-count)]
        
    print(out0)
