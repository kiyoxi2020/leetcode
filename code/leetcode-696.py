'''
leetcode 696. 计数二进制子串

给定一个字符串 s，计算具有相同数量 0 和 1 的非空（连续）子字符串的数量，并且这些子字符串中的所有 0 和所有 1 都是连续的。

重复出现的子串要计算它们出现的次数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/count-binary-substrings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def countBinarySubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s+'$'
        n = len(s)
        list0 = []
        last = s[0]
        count = 1
        out = 0
        for i in range(1, n):
            if s[i] == last: count+=1
            else:
                list0.append(count)
                if len(list0)>1:
                    out += min(list0[-1], list0[-2])
                last = s[i]
                count = 1
        
        return out

