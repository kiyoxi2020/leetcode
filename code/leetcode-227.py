'''
leetcode 227. 基本计算器 II

给你一个字符串表达式 s ，请你实现一个基本计算器来计算并返回它的值。

整数除法仅保留整数部分。

 

示例 1：

输入：s = "3+2*2"
输出：7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/basic-calculator-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        p = ['+', '-', '*', '/']
        stack1 = collections.deque()
        stack2 = collections.deque()
        n = len(s)
        i=0
        while(i<n):
            t = s[i]
            i+=1
            if t not in p and t !=' ':
                while(i< n and ord(s[i])>=48 and ord(s[i])<=57):
                    t+=s[i]
                    i+=1
            if t!=' ':
                if t in p:
                    stack2.append(t)
                else:
                    stack1.append(int(t))
                    if stack2 and (stack2[-1] == '/' or stack2[-1] == '*'):
                        t1, t2 = stack1.pop(), stack1.pop()
                        if stack2[-1]=='/': v = t2//t1
                        else: v = t1*t2
                        stack2.pop()
                        stack1.append(v)
        while(stack2):
            t1, t2 = stack1.popleft(), stack1.popleft()
            if stack2[0]=='+': v = t1+t2
            else: v=t1-t2
            stack2.popleft()
            stack1.appendleft( v)
        out = 0
        while(stack1):
            t = stack1.popleft()
            out = out*10+t
        
        return out


                        

