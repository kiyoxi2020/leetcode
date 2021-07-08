
'''
leetcode 560. 和为K的子数组

给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

示例 1 :

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/subarray-sum-equals-k
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        pre = 0
        dict0 = {}
        count = 0
        for i in range(n):
            pre += nums[i]
            t = pre-k
            if pre == k: count+=1
            if t in dict0: count+=dict0[t]
            if pre in dict0: dict0[pre] += 1
            else: dict0[pre]=1

        return count
