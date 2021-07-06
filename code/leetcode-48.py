'''
leetcode 48. 旋转图像

给定一个 n × n 的二维矩阵 matrix 表示一个图像。请你将图像顺时针旋转 90 度。

你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。请不要 使用另一个矩阵来旋转图像。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-image
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for j in range(n//2):
            for i in range(j, n-1-j):
                matrix[i][n-j-1], matrix[n-j-1][n-i-1], matrix[n-i-1][j], matrix[j][i] = matrix[j][i], matrix[i][n-j-1], matrix[n-j-1][n-i-1], matrix[n-i-1][j]
        return
