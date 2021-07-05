'''
leetcode 461：两个整数之间的 汉明距离 指的是这两个数字对应二进制位不同的位置的数目。

给你两个整数 x 和 y，计算并返回它们之间的汉明距离。
'''
class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        t = x^y
        count = 0
        while(t!=0):
            t, t0 = t//2, t%2
            if t0==1: count+=1
        return count