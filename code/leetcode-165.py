class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        def convert(v):
            v1 = []
            tt = ''
            for i in range(len(v)):
                if v[i] != '.':
                    tt += v[i]
                else:
                    v1.append(int(tt))
                    tt = ''
            if len(tt)!=0: v1.append(int(tt))
            return v1
    
        v1 = convert(version1)
        v2 = convert(version2)
        n1 = len(v1)
        n2 = len(v2)
        if n1>n2:
            while(n1!=n2):
                v2.append(0)
                n2+=1
        elif n1<n2:
            while(n1!=n2):
                v1.append(0)
                n1+=1
        for i in range(n1):
            if v1[i] > v2[i]: return 1
            elif v1[i] < v2[i]: return -1
        return 0