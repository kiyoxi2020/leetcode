'''
leetcode 268. 丢失的数字

给定一个包含 [0, n] 中 n 个数的数组 nums ，找出 [0, n] 这个范围内没有出现在数组中的那个数。
'''

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        out = 0
        for i, j in enumerate(nums):
            out ^= i ^ j
        out ^= len(nums)
        return out



