'''
leetcode 684. 冗余连接

在本问题中, 树指的是一个连通且无环的无向图。

输入一个图，该图由一个有着N个节点 (节点值不重复1, 2, ..., N) 的树及一条附加的边构成。附加的边的两个顶点包含在1到N中间，这条附加的边不属于树中已存在的边。

结果图是一个以边组成的二维数组。每一个边的元素是一对[u, v] ，满足 u < v，表示连接顶点u 和v的无向图的边。

返回一条可以删去的边，使得结果图是一个有着N个节点的树。如果有多个答案，则返回二维数组中最后出现的边。答案边 [u, v] 应满足相同的格式 u < v。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/redundant-connection
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        n = len(edges)
        node_father = [-1] * (n+1)
        node_label = {}
        for i, j in edges:
            i = i
            j = j
            if node_father[i] == -1 and node_father[j] != -1: 
                node_father[i] = node_father[j]
                node_label[node_father[j]].append(i)
            elif node_father[i] != -1 and node_father[j] == -1: 
                node_father[j] = node_father[i]
                node_label[node_father[i]].append(j)
            elif node_father[i] == -1 and node_father[j] == -1:
                node_father[i] = i
                node_label[i] = [i]
                node_father[j] = node_father[i]
                node_label[i].append(j)
            elif node_father[j] != node_father[i]:
                t1 = min(node_father[j], node_father[i])
                t2 = max(node_father[j], node_father[i])
                for k in node_label[t2]:
                    node_father[k] = t1
                    node_label[t1].append(k)
                del node_label[t2]
            elif node_father[j] == node_father[i]:
                return [i, j]
        return []
            