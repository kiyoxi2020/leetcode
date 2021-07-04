'''
leetcode 238：除自身之外的数组的乘积，给定长度为n的整数数组nums，其中n>1，
返回输出数组output，其中output[i]等于nums中除nums[i]之外的其余元素的乘积

解法：从左往右计算一遍乘积，得到数组left，从右往左计算一遍乘积，得到数组right，这样对于每个点，都可得到左边的乘积和右边的乘积，两者相乘即可

'''
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        left = [0]*n
        right = [0]*n
        left[0] = nums[0]
        right[n-1] = nums[n-1]
        for i in range(1,n):
            left[i] = left[i-1]*nums[i]
            right[n-i-1] = right[n-i]*nums[n-i-1]
        out = [0]*n
        for i in range(n):
            if i==0: out[i] = right[i+1]
            elif i==n-1: out[i] = left[i-1]
            else: out[i] = left[i-1]*right[i+1]
        return out