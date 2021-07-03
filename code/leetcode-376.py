'''
leetcode 376：摆动序列，若连续数字之间的差严格地在正数、负数之间交替，
则称该序列为摆动序列，给定一个整数数组nums，返回nums中作为摆动序列的最长子序列长度，
子序列可以通过从原始序列中删除一些元素获得，剩下的元素保持原始顺序
'''
class Solution(object):
    '''
    解法1：1、dp1[i]表示以第i个数字结尾的摆动序列的最长长度，
    dp2[i]表示该最长序列最后一个差值；
    2、if (nums[i]-nums[j])*dp2[j]<0: 
    if dp1[j]+1>dp1[i]: 
        dp1[i]=dp1[j]+1 dp2[i]=nums[i]-nums[j] 
        对j进行遍历，复杂度为O(n^2)
    '''
    def wiggleMaxLength1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 1: return n
        if n == 2: 
            if nums[1]-nums[0]!=0: return 2
            else: return 1
        dp1 = [0]*n
        dp2 = [0]*n
        dp1[0] = 1
        dp2[1] = nums[1]-nums[0]
        if dp2[1]!=0:
            dp1[1] = 2
        else:
            dp1[1] = 1
        for i in range(2,n):
            for k in range(1,i+1):
                j = i-k
                if (nums[i]-nums[j])*dp2[j]<0 or (dp2[j]==0 and nums[i]-nums[j]!=0):
                    if dp1[j]+1>dp1[i]:
                        dp1[i]=dp1[j]+1
                        dp2[i]=nums[i]-nums[j]
        
        return max(dp1)

    '''
    解法2：1、up[i]表示以第i个数字结尾，且结尾上升的摆动序列，down[i]表示以第i个数字结尾，
    且结尾下降的摆动序列；
    2、up[i]=max(up[i-1], down[i-1]+1) 
    if nums[i]>nums[i-1] else up[i-1]；
    down[i]=max(down[i-1], up[i-1]+1) if nums[i]<nums[i-1] else: down[i-1] ，
    复杂度为O(n)
    '''
    def wiggleMaxLength2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        up = [0] * n
        down = [0] * n
        up[0] = 1
        down[0] = 1
        for i in range(1, n):
            if nums[i] > nums[i-1]:
                up[i] = max(up[i], down[i-1]+1)
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = max(down[i-1], up[i-1]+1)
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]
        
        return max([max(up), max(down)])
        