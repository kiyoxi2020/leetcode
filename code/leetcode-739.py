'''
leetcode 739. 每日温度

请根据每日 气温 列表，重新生成一个列表。对应位置的输出为：要想观测到更高的气温，至少需要等待的天数。如果气温在这之后都不会升高，请在该位置用 0 来代替。

例如，给定一个列表 temperatures = [73, 74, 75, 71, 69, 72, 76, 73]，你的输出应该是 [1, 1, 4, 2, 1, 1, 0, 0]。

提示：气温 列表长度的范围是 [1, 30000]。每个气温的值的均为华氏度，都是在 [30, 100] 范围内的整数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/daily-temperatures
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        stack = []
        stack.append([0, temperatures[0]])
        n = len(temperatures)
        out = [0]*n
        for i in range(1, n):
            if temperatures[i] > stack[-1][1]:
                j = 1
                while(j<=len(stack) and stack[-j][1]<temperatures[i]):
                    out[stack[-j][0]]=i-stack[-j][0]
                    stack.pop(-j)
                stack.append([i, temperatures[i]])
            else:
                stack.append([i, temperatures[i]])
                
        return out
