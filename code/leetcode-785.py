'''
leetcode 785. 判断二分图

存在一个 无向图 ，图中有 n 个节点。其中每个节点都有一个介于 0 到 n - 1 之间的唯一编号。给你一个二维数组 graph ，其中 graph[u] 是一个节点数组，由节点 u 的邻接节点组成。形式上，对于 graph[u] 中的每个 v ，都存在一条位于节点 u 和节点 v 之间的无向边。该无向图同时具有以下属性：
不存在自环（graph[u] 不包含 u）。
不存在平行边（graph[u] 不包含重复值）。
如果 v 在 graph[u] 内，那么 u 也应该在 graph[v] 内（该图是无向图）
这个图可能不是连通图，也就是说两个节点 u 和 v 之间可能不存在一条连通彼此的路径。
二分图 定义：如果能将一个图的节点集合分割成两个独立的子集 A 和 B ，并使图中的每一条边的两个节点一个来自 A 集合，一个来自 B 集合，就将这个图称为 二分图 。

如果图是二分图，返回 true ；否则，返回 false 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/is-graph-bipartite
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        dict0 = {}
        n = len(graph)
        dict0[0] = 0
        list0 = [i for i in range(n)]
        list1 = [0]
        ind = 0
        while(1):
            if len(dict0)==n: break
            if ind>=len(dict0):
                t = list0[0]
                list0.pop(0)
            else:
                t = list1[0]
                list1.pop(0)
            if t in list0: list0.remove(t)
            if t in dict0:
                flag = dict0[t]
            else: 
                flag=0
                dict0[t] = flag
            ind+=1
            for i in graph[t]:
                if i not in dict0: dict0[i] = 1-flag
                elif dict0[i]!=1-flag: return False
                if i in list0: 
                    list0.remove(i)
                    list1.append(i)
        
        for i in range(1, n):
            flag = dict0[i]
            for j in graph[i]:
                if dict0[j] != 1-flag: return False

        return True