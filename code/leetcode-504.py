'''
leetcode 504：七进制数，给定一个整数n，将其转化为7进制

解法：除7取余数
'''
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0: return '0'
        out = []
        sign = ''
        if num < 0: sign = '-'
        num = abs(num)
        while(num!=0):
            num, num2 = num//7, num%7
            out.insert(0, num2)
        sign += ''.join(str(i) for i in out)
        return sign