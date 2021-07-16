
'''
HJ8 合并表记录

描述
数据表记录包含表索引和数值（int范围的正整数），请对表索引相同的记录进行合并，即将相同索引的数值进行求和运算，输出按照key值升序进行输出。

输入描述：
先输入键值对的个数
然后输入成对的index和value值，以空格隔开

输出描述：
输出合并后的键值对（多行）


'''
while(1):
    try:
        n = int(raw_input())
        d = {}
        for i in range(n):
            data = [int(i) for i in raw_input().split(' ')]
            if data[0] in d:
                d[data[0]] += data[1]
            else:
                d[data[0]] = data[1]
        keys = d.keys()
        keys.sort()
        for i in keys:
            print(str(i) + ' ' + str(d[i]))
    except:
        break
                