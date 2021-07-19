'''
LCP 08. 剧情触发时间

在战略游戏中，玩家往往需要发展自己的势力来触发各种新的剧情。一个势力的主要属性有三种，分别是文明等级（C），资源储备（R）以及人口数量（H）。在游戏开始时（第 0 天），三种属性的值均为 0。

随着游戏进程的进行，每一天玩家的三种属性都会对应增加，我们用一个二维数组 increase 来表示每天的增加情况。这个二维数组的每个元素是一个长度为 3 的一维数组，例如 [[1,2,1],[3,4,2]] 表示第一天三种属性分别增加 1,2,1 而第二天分别增加 3,4,2。

所有剧情的触发条件也用一个二维数组 requirements 表示。这个二维数组的每个元素是一个长度为 3 的一维数组，对于某个剧情的触发条件 c[i], r[i], h[i]，如果当前 C >= c[i] 且 R >= r[i] 且 H >= h[i] ，则剧情会被触发。

根据所给信息，请计算每个剧情的触发时间，并以一个数组返回。如果某个剧情不会被触发，则该剧情对应的触发时间为 -1 。

示例 1：

输入： increase = [[2,8,4],[2,5,0],[10,9,8]] requirements = [[2,11,3],[15,10,7],[9,17,12],[8,1,14]]

输出: [2,-1,3,-1]

解释：

初始时，C = 0，R = 0，H = 0

第 1 天，C = 2，R = 8，H = 4

第 2 天，C = 4，R = 13，H = 4，此时触发剧情 0

第 3 天，C = 14，R = 22，H = 12，此时触发剧情 2

剧情 1 和 3 无法触发。

https://leetcode-cn.com/problems/ju-qing-hong-fa-shi-jian/

'''
class Solution(object):
    def getTriggerTime(self, increase, requirements):
        """
        :type increase: List[List[int]]
        :type requirements: List[List[int]]
        :rtype: List[int]
        """
        st = [0, 0, 0]
        n = len(requirements)
        req_c = [[requirements[i][0], i] for i in range(n)]
        req_r = [[requirements[i][1], i] for i in range(n)]
        req_h = [[requirements[i][2], i] for i in range(n)]
        req_c.sort()
        req_r.sort()
        req_h.sort()
        reach = [0]*n
        sum_c, sum_r, sum_h = 0, 0, 0
        i_c, i_r, i_h = 0, 0, 0
        out = [-1]*n
        count = 0
            
        def repeat(req, sum0, i, count):
            while(i<n and req[i][0]<=sum0):
                ind = req[i][1]
                reach[ind] += 1
                if reach[ind] == 3: out[ind] = count
                i+=1
            return i
        i_c = repeat(req_c, sum_c, i_c, count)
        i_r = repeat(req_r, sum_r, i_r, count)
        i_h = repeat(req_h, sum_h, i_h, count)
        for c, r, h in increase:
            sum_c, sum_r, sum_h = sum_c+c, sum_r+r, sum_h+h
            count += 1
            i_c = repeat(req_c, sum_c, i_c, count)
            i_r = repeat(req_r, sum_r, i_r, count)
            i_h = repeat(req_h, sum_h, i_h, count)
        
        return out