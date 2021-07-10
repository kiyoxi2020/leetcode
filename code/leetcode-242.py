'''
leetcode 242. 有效的字母异位词

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词（包含的字符及数量是否相同）。
'''
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)!=len(t): return False
        dict0 = {}
        for i in s:
            if i in dict0: dict0[i]+=1
            else: dict0[i]=1
        for j in t:
            if j in dict0: 
                dict0[j]-=1
                if dict0[j] < 0: return False
            else:
                return False
        return True
