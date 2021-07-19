'''
LCP 04. 覆盖

你有一块棋盘，棋盘上有一些格子已经坏掉了。你还有无穷块大小为1 * 2的多米诺骨牌，你想把这些骨牌不重叠地覆盖在完好的格子上，请找出你最多能在棋盘上放多少块骨牌？这些骨牌可以横着或者竖着放。

 

输入：n, m代表棋盘的大小；broken是一个b * 2的二维数组，其中每个元素代表棋盘上每一个坏掉的格子的位置。

输出：一个整数，代表最多能在棋盘上放的骨牌数。

 

示例 1：

输入：n = 2, m = 3, broken = [[1, 0], [1, 1]]
输出：2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/broken-board-dominoes
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def domino(self, n, m, broken):
        """
        :type n: int
        :type m: int
        :type broken: List[List[int]]
        :rtype: int
        """
        matrix = [[0] * m for _ in range(n)]
        match = [[[] for _ in range(m)] for _ in range(n)]
        for i, j in broken:
            matrix[i][j] = 1
        count = 0

        def find(i, j):
            for di, dj in [[0,1],[1,0],[-1,0],[0,-1]]:
                i_n = i+di
                j_n = j+dj
                if i_n<n and j_n<m and i_n>=0 and j_n>=0:
                    flag = 0
                    if matrix[i_n][j_n]==0:
                        flag = 1
                    else:
                        if len(match[i_n][j_n])>0:
                            # matrix[i_n][j_n] = 1
                            i_t, j_t = match[i_n][j_n]
                            match[i_n][j_n] = []
                            if find(i_t, j_t):
                                flag = 1
                            else:
                                # matrix[i_n][j_n] = 0
                                match[i_n][j_n] = [i_t, j_t]
                    if flag == 1:
                        matrix[i][j] = 1
                        matrix[i_n][j_n]=1
                        match[i][j] = [i_n, j_n]
                        match[i_n][j_n] = [i, j]
                        return True
            return False

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if find(i, j):
                        count+=1
                   
        return count