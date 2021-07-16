'''
HJ6 质数因子

输入描述：
输入一个long型整数

输出描述：
按照从小到大的顺序输出它的所有质数的因子，以空格隔开。最后一个数后面也要有空格。

示例1
输入：
180

输出：
2 2 3 3 5



'''
def compute(n, out):
    i = 2
    while(i<n):
        if i*i>n: break
        if n%i == 0:
            out.append(i)
            return compute(n//i, out)
        i+=1
    out.append(n)
    return out

while(1):
    try:
        data = int(input())
        out = compute(data, [])
        print(' '.join(str(i) for i in out)+' ')
    except:
        break