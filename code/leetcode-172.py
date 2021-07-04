'''
leetcode 172：阶乘后的零，给定整数n，返回阶乘n！尾数中0的数量

解法：考虑到尾数中的0都是由2*5得到的，因此可以计算1, 2, ..., n中含有因子2、5的数量；
计算因子数量时，首先计算1~n中5及5的倍数的数量，然后计算1~n/5中的数量，依次类推
'''
class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """

        def count(x, a):
            if x < a: return 0
            num = 0
            t = 1
            while(a*t<=x):
                num+=1
                t+=1
            num += count(x//a, a)
            return num
        
        # num_2 = count(n,2)
        num_5 = count(n,5)
        
        return num_5