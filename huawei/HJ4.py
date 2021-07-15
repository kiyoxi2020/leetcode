'''
HJ4 字符串分隔

描述
•连续输入字符串，请按长度为8拆分每个字符串后输出到新的字符串数组；
•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。

输入描述：
连续输入字符串(输入多次,每个字符串长度小于100)

输出描述：
输出到长度为8的新字符串数组
'''
while(1):
    try:
        data = input()
        if data == '': continue
        L = len(data)
        if L%8!=0: data += '0' * (8-L%8)
        L = len(data)
        ind = 0
        while(ind+8 <= L):
            print(data[ind:ind+8])
            ind = ind+8
            
    except:
        break
    
        