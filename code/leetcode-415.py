class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = len(num1)
        n2 = len(num2)
        c = 0
        out = 0
        count = 0
        out_str = ''
        while(1):
            if n1<=0 and n2<=0 and c == 0: break
            if n1 <= 0: t1 = 0
            else: t1 = int(num1[n1-1])
            if n2 <= 0: t2 = 0
            else: t2 = int(num2[n2-1])
            out1 = (t1+t2+c)%10
            c = (t1+t2+c)//10
            n1-=1
            n2-=1
            out += out1*(10**count)
            out_str = str(out1) + out_str
            count+=1
        return out_str
            