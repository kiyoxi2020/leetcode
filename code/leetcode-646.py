'''
leetcode 646：最长数对链，给出n个数对(a, b)，每个数对的第一个数比第二个数小，
定义跟随关系：当且仅当b<c，数对(a, b)之后可以接(c, d)，给定一个数对集合，
找出能够形成最长对链的长度


解法：1、首先按照第二个数进行升序排列，保证每次最先选结尾在前面的；
2、dp[i]表示到第i个数对为止，所选序列的结尾位置，
if pairs[i][0]>dp[i-1]: dp[i]=pairs[i][1] count+=1 else: dp[i]=dp[i-1]
3、输出count
'''

class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        pairs.sort(key=lambda x: x[1])
        n = len(pairs)
        dp = [float("inf")] * n
        dp[0] = pairs[0][1]
        nums = 0
        count = 1
        for j in range(1, n):
            if pairs[j][0] > dp[j-1]: 
                dp[j] = pairs[j][1]
                count += 1
            else:
                dp[j] = dp[j-1]
        
        return count

    
s = Solution()
print(s.findLongestChain([[1,2], [2,3], [3,4]]))
