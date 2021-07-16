'''
1. DNS分层域名系统
题目大意：给定几行两组的域名列表，输出完整域名，并且要按序输出。

输入：
第一行为整数N（N不大于20），后续N行，每行一个域名及其父域名组成，中间用空格分隔。最后一行为指定的顶级域名。
如：
5
www huawei
career huawei
google com
huawei com
sina com
com

输出：
按顶级域名升序输出。如com下的为
career.huawei.com
google.com
sina.com
www.huawei.com
————————————————
版权声明：本文为CSDN博主「Huntermanwp」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/Huntermanwp/article/details/117981494

'''
def compute(data, address):
    list0 = set()
    out = []
    for i, j in data:
        if j == address:
            if i not in list0:
                list0.add(i)
                out.append(i+'.'+address)
        else:
            list0.add(j)
            out.append(i+'.'+j+'.'+address)
    out.sort()
    for i in out:
        print(i)
    return


while(1):
    try:
        n = int(input())
        data = []
        for i in range(n):
            t = [i for i in input().split()]
            data.append(t)
        address = input()
        compute(data, address)
    except:
        break
        