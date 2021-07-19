'''
LCP 05. 发 LeetCoin

力扣决定给一个刷题团队发LeetCoin作为奖励。同时，为了监控给大家发了多少LeetCoin，力扣有时候也会进行查询。

 

该刷题团队的管理模式可以用一棵树表示：

团队只有一个负责人，编号为1。除了该负责人外，每个人有且仅有一个领导（负责人没有领导）；
不存在循环管理的情况，如A管理B，B管理C，C管理A。
 

力扣想进行的操作有以下三种：

给团队的一个成员（也可以是负责人）发一定数量的LeetCoin；
给团队的一个成员（也可以是负责人），以及他/她管理的所有人（即他/她的下属、他/她下属的下属，……），发一定数量的LeetCoin；
查询某一个成员（也可以是负责人），以及他/她管理的所有人被发到的LeetCoin之和。
 

输入：

N表示团队成员的个数（编号为1～N，负责人为1）；
leadership是大小为(N - 1) * 2的二维数组，其中每个元素[a, b]代表b是a的下属；
operations是一个长度为Q的二维数组，代表以时间排序的操作，格式如下：
operations[i][0] = 1: 代表第一种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
operations[i][0] = 2: 代表第二种操作，operations[i][1]代表成员的编号，operations[i][2]代表LeetCoin的数量；
operations[i][0] = 3: 代表第三种操作，operations[i][1]代表成员的编号；
输出：

返回一个数组，数组里是每次查询的返回值（发LeetCoin的操作不需要任何返回值）。由于发的LeetCoin很多，请把每次查询的结果模1e9+7 (1000000007)。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/coin-bonus
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def buildTree(self, lead):
        list0 = []
        n = len(lead)
        range0 = [[] for _ in range(n)]

        def dfs(i):
            l = len(list0)
            r = len(list0)
            list0.append(i)
            if len(lead[i])==0: 
                range0[i] = [l, r]
                return [l, r]
            for j in lead[i]:
                l0,r0 = dfs(j)
                l = min(l, l0)
                r = max(r, r0)
            range0[i] = [l, r]
            return [l, r]
        
        dfs(0)
        maps = [0]*n
        maps_range = [[] for _ in range(n)]
        for i in range(n):
            maps[list0[i]] = i
            maps_range[i] = range0[list0[i]]

        tree = [0] * (2*n)
        return maps, maps_range, tree
    
    def updateTree(self, map_id, coin, trees, n):
        map_id += n
        trees[map_id] += coin
        map_id/=2
        while(map_id>0):
            trees[map_id] = trees[2*map_id] + trees[2*map_id+1]
            map_id/=2
        return
    
    def searchRange(self, range_id, tree, n):
        l = range_id[0]+n
        r = range_id[1]+n
        sum0 = 0
        while(l<=r):
            if l%2==1:
                sum0+=tree[l]
                l+=1
            if r%2==0:
                sum0+=tree[r]
                r-=1
            l/=2
            r/=2
        return sum0


    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        lead = [[] for _ in range(n)]
        
        out = []
        for i,j in leadership:
            lead[i-1].append(j-1)
        
        maps, ranges, trees = self.buildTree(lead)

        for op in operations:
            if op[0] == 1:
                id = op[1]-1
                coin = op[2]
                map_id = maps[id]
                self.updateTree(map_id, coin, trees, n)
                
            elif op[0] == 2:
                id, coin = op[1]-1, op[2]
                stack = [id]
                while(len(stack) > 0):
                    id = stack.pop(0)
                    self.updateTree(maps[id], coin, trees, n)
                    for i in lead[id]:
                        stack.append(i)
            else:
                id = op[1]-1
                range_id = ranges[maps[id]]
                sum0 = self.searchRange(range_id, trees, n)
                out.append(sum0%1000000007)
        return out