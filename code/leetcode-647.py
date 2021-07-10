'''
leetcode 647. 回文子串

给定一个字符串，你的任务是计算这个字符串中有多少个回文子串。

具有不同开始位置或结束位置的子串，即使是由相同的字符组成，也会被视作不同的子串。


'''
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        count = 0

        for i in range(n):
            k = 0
            while(i-k>=0 and i+k<n):
                if s[i-k]==s[i+k]:
                    count+=1
                else:
                    break
                k+=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                k=0
                while(i-k>=0 and i+1+k<n):
                    if s[i-k]==s[i+1+k]:
                        count+=1
                    else:
                        break
                    k+=1
        return count
