'''
LCP 03. 机器人大冒险

力扣团队买了一个可编程机器人，机器人初始位置在原点(0, 0)。小伙伴事先给机器人输入一串指令command，机器人就会无限循环这条指令的步骤进行移动。指令有两种：

U: 向y轴正方向移动一格
R: 向x轴正方向移动一格。
不幸的是，在 xy 平面上还有一些障碍物，他们的坐标用obstacles表示。机器人一旦碰到障碍物就会被损毁。

给定终点坐标(x, y)，返回机器人能否完好地到达终点。如果能，返回true；否则返回false。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/programmable-robot
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def bonus(self, n, leadership, operations):
        """
        :type n: int
        :type leadership: List[List[int]]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        coins = [0] * (n+1)
        coins_sum = [0] * (n+1)
        lead = [[] for _ in range(n+1)]
        
        lead_sum = [0] * (n+1)
        out = []
        for i,j in leadership:
            lead[i].append(j)
        for i in range(1, n+1):
            stack = [ j for j in lead[i]]
            count = 0
            while(len(stack)>0):
                id = stack.pop(0)
                count+=1
                for j in lead[id]:
                    stack.append(j)
            lead_sum[i] = count
            
        for op in operations:
            if op[0] == 1:
                id = op[1]
                coin = op[2]
                coins[id] += coin
                coins_sum[id] += coin
            elif op[0] == 2:
                id, coin = op[1], op[2]
                stack = [id]
                while(len(stack) > 0):
                    id = stack.pop(0)
                    coins[id] += coin
                    coins_sum[id] += coin *(lead_sum[id]+1)
                    for i in lead[id]:
                        stack.append(i)
            else:
                id = op[1]
                sum0 = 0
                stack = [id]
                while(len(stack)>0):
                    id = stack.pop(0)
                    sum0+=coins[id]
                    for i in lead[id]:
                        stack.append(i)
                out.append(sum0)
        return out
                


