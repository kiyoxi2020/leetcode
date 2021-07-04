'''
面试题 05.03. 翻转数位
给定一个32位整数 num，你可以将一个数位从0变为1。请编写一个程序，找出你能够获得的最长的一串1的长度。

'''
class Solution(object):
    def reverseBits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def convert(x):
            sign=0
            if x<0: sign=1
            out = []
            x=abs(x)
            if x == 0: return [0]
            while(x>0):
                x, t = x//2, x%2
                out.insert(0, t)
            if len(out) <= 32: out = [0]*(32-len(out))+out
            if sign==1:
                out = [1-i for i in out]
                if out[31]==0: out[31]=1
                else:
                    i = 31
                    while(i>=0):
                        if out[i]==1: 
                            out[i]=0
                            i-=1
                        else: break
                    if i>=0: out[i]=1
            return out
        
        num_2 = convert(num)
        n = len(num_2)
        count = 0
        max0 = 0
        num_0 = 0
        last_0_pos = 0
        for i in range(n):
            if num_2[i] == 1: count+=1
            else:
                num_0+=1
                if num_0 == 2:
                    max0=max(max0, count)
                    count=i-last_0_pos
                    num_0= 1
                    last_0_pos = i
                else:
                    last_0_pos=i
                    count+=1
        max0=max(max0, count)
        return max0

