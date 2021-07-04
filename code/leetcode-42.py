'''
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

'''
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        n = len(height)
        if n<3:return 0
        left = [0] * n
        max0 = height[0]
        for i in range(1, n):
            if height[i] > max0: max0 = height[i]
            else: left[i] = max0-height[i]
        right = [0] * n
        max0 = height[n-1]
        for i in range(n-1,-1,-1):
            if height[i] > max0: max0 = height[i]
            else: right[i] = max0-height[i]
            right[i] = min(right[i], left[i])
        return sum(right)