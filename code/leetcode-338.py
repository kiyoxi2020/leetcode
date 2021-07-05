'''
leetcode 338. 比特位计数
给定一个非负整数 num。对于 0 ≤ i ≤ num 范围中的每个数字 i ，计算其二进制数中的 1 的数目并将它们作为数组返回。
'''
class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        out = [0] * (n+1)
        for i in range(1,n+1,1):
            if i%2==1: out[i]=out[i-1]+1
            else:
                out[i]=out[i>>1]
        
        return out