'''
leetcode 204：计数质数，统计所有小于n的质数

解法：埃氏筛法，从1到n遍历，当前遍历到m，则把所有是m的倍数且小于n的数标为合数，统计剩下的数
'''
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        out = [1] * (n-2)
        for i in range(n-2):
            t = i+2
            if out[i] == 1:
                j = 2
                while(j*t<n):
                    out[j*t-2]=0
                    j+=1    
        return sum(out)