'''
leetcode 210. 课程表 II



'''
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        n = numCourses
        in_degree = [0] * n
        edge_in = [[] for _ in range(n)]
        for i,j in prerequisites:
            edge_in[j].append(i)
            in_degree[i] += 1
        queue = [i for i in range(n) if in_degree[i] == 0]
        out = []
        while(queue):
            ind = queue.pop(0)
            out.append(ind)
            for i in edge_in[ind]:
                in_degree[i]-=1
                if in_degree[i] == 0:
                    queue.append(i)
        if len(out) == n: return out
        else: return []
        
        