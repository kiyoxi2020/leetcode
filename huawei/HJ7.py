'''
HJ7 取近似值

描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于5,向上取整；小于5，则向下取整。

输入描述：
输入一个正浮点数值

输出描述：
输出该数值的近似整数值

'''
while(1):
    try:
        data = float(input())
        print(int(round(data)))
    except:
        break