'''
给定一个只包含数字的字符串，用以表示一个 IP 地址，返回所有可能从 s 获得的 有效 IP 地址 。你可以按任何顺序返回答案。

有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        out = []

        def dfs(str0, list0):
            n = len(str0)
            if len(list0) == 4 and n != 0:
                return
            if n == 0:
                if len(list0) == 4:
                    out.append('.'.join(list0))
                return
            for i in range(n):
                t = int(str0[0:i+1])
                if str0[0] == '0' and i>0: continue
                if t<=255 and t>=0:
                    list0.append(str0[0:i+1])
                    dfs(str0[i+1:], list0)
                    list0.pop(-1)
            return 

        dfs(s,[])
        return out