'''
HJ5 进制转换

描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

输入描述：
输入一个十六进制的数值字符串。注意：一个用例会同时有多组输入数据，请参考帖子https://www.nowcoder.com/discuss/276处理多组输入的问题。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。

'''

while(1):
    try:
        data = input()
        n = len(data)
        out = 0
        for i in range(2, n):
            t = data[i]
            if ord(t)>= 65 and ord(t) <= 70:
                t = ord(t)-65+10
            else: t = int(t)
            out = out*16+t
        print(out)
    except:
        break
        
    