'''
leetcode 476. 数字的补数

给你一个 正 整数 num ，输出它的补数。补数是对该数的二进制表示取反。

'''
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        t = 0
        count = 0
        while(1):
            t0=(1-num%2)
            t += t0* (2**count)
            count += 1
            num=num//2
            if num==0: break
            
        return t
        
            
