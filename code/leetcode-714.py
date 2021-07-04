'''
leetcode 714：买卖股票的最佳时机含手续费，给定prices表示股票每天价格，
fee表示交易股票费用，可以无限次交易，但每次交易需手续费，如果已经购买了一个股票，得先卖出才能买入

解法：构建状态转移矩阵，1、buy[i]表示第i天买入的最大收入，sell[i]表示第i天卖出的最大收入；
2、buy[i]=max(buy[i-1], sell[i-1]-prices[i])，sell[i]=max(sell[i-1], buy[i-1]+prices[i]-fee)
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        n = len(prices)
        buy = [0] * n
        sell = [0] * n
        buy[0] = -prices[0]
        for i in range(1, n):
            buy[i] = max(buy[i-1], sell[i-1]-prices[i])
            sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)

        return sell[n-1]