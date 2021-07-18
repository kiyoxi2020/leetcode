'''
2.推箱子游戏

给一组长度为N的整数字符串，每个箱子最终的位置，要求是把所有箱子都从0推到最终位置，
允许连续的箱子一起推，比如2，3，4号箱子都需要前进的话，推一次就可以，输出最少的推动次数。

'''
def compute(data):

    def divide(data0):
        if len(data0)==1: return(data0[0])
        else:
            count = 0
            min0 = min(data0)
            count += min0
            data1 = [i-min0 for i in data0]
            st = 0
            n = len(data1)
            while(data1[st]==0):
                st+=1
            ed = st
            while(ed<n):
                if data1[ed]!=0: ed+=1
                else:
                    count += divide(data1[st:ed])
                    st = ed
                    while(st<n and data1[st]==0): st+=1
                    ed = st
            if ed>st: count += divide(data1[st:ed])
            return count
    
    return divide(data)


print(compute([1, 3, 4, 1, 10, 2, 6, 8]))