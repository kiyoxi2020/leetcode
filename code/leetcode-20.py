'''
leetcode 20. 有效的括号

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict0 = {'(':')','{':'}','[':']'}
        stack = []
        for i in s:
            if len(stack)==0: stack.append(i)
            else:
                if stack[-1] in dict0.keys() and dict0[stack[-1]] == i:
                    stack.pop(-1)
                else:
                    stack.append(i)
        return len(stack)==0