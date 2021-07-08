class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dict0 = {}
        for i in nums:
            dict0[i] = 1
        t = [i for i in dict0.keys() if dict0[i]==1 ]
        t.sort()
        t.append(float('inf'))
        left = 0
        max0 = 0
        for i in range(1, len(t),1):
            if t[i]-t[i-1]>1:
                max0 = max(max0, i-left)
                left = i
        
        return max0

