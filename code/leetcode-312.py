class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        def solve(ind1, ind2):
            if ind1-ind2>=0:
                return nums[ind1]
            max0 = 0
            for i in range(ind1+1, ind2):
                t = nums[ind1] * nums[ind2] * nums[i]
                t += solve(ind1, i) + solve(i, ind2)
                max0 = max(max0, t)
            return max0
        
        return solve(0, len(nums)-1)
        
a = Solution()
print(a.maxCoins([3,1,5,8]))

# def maxCoins(self, nums):
#     """
#     :type nums: List[int]
#     :rtype: int
#     """
#     out = []

#     def dfs(nums0, sum0):
#         n = len(nums0)
#         if n == 1:
#             out.append(sum0+nums0[0])
#             return
#         for i in range(n):
#             t = nums0[i]
#             left = 1 if i==0 else nums0[i-1]
#             right = 1 if i==n-1 else nums0[i+1]
#             nums0.pop(i)
#             dfs(nums0, sum0+left*right*t)
#             nums0.insert(i, t)
#         return 

#     dfs(nums, 0)
#     return max(out)