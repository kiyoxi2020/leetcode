'''
leetcode 190. 颠倒二进制位
颠倒给定的 32 位无符号整数的二进制位。
'''
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        out = 0
        count = 0
        while(1):
            out+=(n&1)
            out = out<<1
            n = n>>1
            count+=1
            if count == 31: break
        out+=(n&1)
        return out