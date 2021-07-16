'''
HJ9 提取不重复的整数

描述
输入一个int型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是0。
输入描述：
输入一个int型整数

输出描述：
按照从右向左的阅读顺序，返回一个不含重复数字的新的整数

'''
while(1):
    try:
        data = raw_input()
        out = 0
        d = set()
        for i in data[::-1]:
            if i not in d:
                d.add(i)
                out = out*10 + int(i)
        print(out)
    except:
        break
            
            