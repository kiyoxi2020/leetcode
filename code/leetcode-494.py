'''
leetcode 494：目标和，给定一个整数数组nums，和一个整数target，向每个整数前添加‘+’或‘-’，
然后串联得到一个表达式，返回结果等于target的不同表达式的数目

解法：考虑pos-neg=target, pos+neg=sum，可得neg=(sum-target)/2，
相当于0-1背包，从数组中找出所有和为neg的组合：1. dp[i][j]表示使用前j个数得到和为i的组合数；
2. dp[i][j]=dp[i][j]+dp[i-nums[j]][j-1]+dp[i][j-1]，分别对应选中第i个数和不选第i个数
'''
class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        sum0 = sum(nums)
        if (sum0-target)%2 != 0: return 0
        neg = (sum0-target)//2
        if neg < 0: return 0
        n = len(nums)
        dp = [[0] * n for _ in range(neg+1)]
        dp[0][0] = 1
        if nums[0] < neg+1:
            dp[nums[0]][0] += 1
        for i in range(1, n):
            for j in range(0,neg+1):
                if j-nums[i] >= 0:
                    dp[j][i] += dp[j-nums[i]][i-1]
                dp[j][i] += dp[j][i-1]

        
        return (dp[neg][n-1])
                

print(Solution().findTargetSumWays([1,1,1,1,1], 3))
