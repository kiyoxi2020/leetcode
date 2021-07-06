class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        out = []
        t = [0] * n
        for i in nums:
            t[i-1]=1
        for i in range(n):
            if t[i]==0: out.append(i+1)
            
        return out