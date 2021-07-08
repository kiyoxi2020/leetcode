'''
leetcode 304. 二维区域和检索 - 矩阵不可变

给定一个二维矩阵，计算其子矩形范围内元素的总和，该子矩阵的左上角为 (row1, col1) ，右下角为 (row2, col2) 。

'''
class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        m, n = len(matrix), len(matrix[0])
        self.sum = [[0] * n for _ in range(m)]
        self.sum[0][0] = matrix[0][0]
        for i in range(1, n, 1):
            self.sum[0][i] = self.sum[0][i-1] + matrix[0][i]
        for j in range(1, m, 1):
            self.sum[j][0] = self.sum[j-1][0] + matrix[j][0]
        for i in range(1, m):
            for j in range(1, n):
                self.sum[i][j] = self.sum[i-1][j] + self.sum[i][j-1] + matrix[i][j] - self.sum[i-1][j-1]
        return


    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if row1>0 and col1>0:
            return self.sum[row2][col2] - self.sum[row1-1][col2] - self.sum[row2][col1-1] + self.sum[row1-1][col1-1]
        elif row1>0:
            return self.sum[row2][col2] - self.sum[row1-1][col2]
        elif col1>0:
            return self.sum[row2][col2] - self.sum[row2][col1-1]
        else:
            return self.sum[row2][col2]





# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)