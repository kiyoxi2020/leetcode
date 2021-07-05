'''
leetcode 318. 最大单词长度乘积
给定一个字符串数组 words，找到 length(word[i]) * length(word[j]) 的最大值，并且这两个单词不含有公共字母。你可以认为每个单词只包含小写字母。如果不存在这样的两个单词，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/maximum-product-of-word-lengths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """

        dict0 = {}
        max0 = 0
        n = len(words)
        for i in range(n):
            w1 = words[i]
            t = 0
            for j in w1:
                t = t|(1<<(ord(j)-97))
            dict0[w1] = t
            for j in range(0, i, 1):
                if dict0[words[j]] & t == 0:
                    max0=max(len(words[j])*len(w1), max0)
        
        return max0

                