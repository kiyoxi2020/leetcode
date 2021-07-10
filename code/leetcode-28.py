'''
leetcode 28. 实现 strStr()

实现 strStr() 函数。

给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如果不存在，则返回  -1 。

 

说明：

当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。

对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/implement-strstr
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        def next(s0):
            n = len(s0)
            out = [0]*n
            for i in range(n):
                k =i
                while(k>0):
                    if s0[0:k]==s0[i-k+1:i+1]: break
                    k-=1
                out[i] = k
            return out
        
        n = len(haystack)
        m = len(needle)
        if m==0: return 0
        needle_next = next(needle)
        i, j = 0, 0
        while(i<n and j<m):
            if i==117:
                i=117
            if haystack[i] == needle[j]:
                i+=1
                j+=1
            else:
                if j>0:
                    j=needle_next[j-1]
                else:
                    i+=1
        if j==m: return i-m
        return -1
                


