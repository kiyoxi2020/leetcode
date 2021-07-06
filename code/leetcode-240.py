'''
leetcode 240. 搜索二维矩阵 II

编写一个高效的算法来搜索 m x n 矩阵 matrix 中的一个目标值 target 。该矩阵具有以下特性：

每行的元素从左到右升序排列。
每列的元素从上到下升序排列。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-a-2d-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m, n = len(matrix), len(matrix[0])
        def search(ind1, ind2):
            if ind1>=m or ind1 <0 or ind2>=n or ind2<0: return False
            if matrix[ind1][ind2]==target: return True
            if matrix[ind1][ind2]<target:
                return search(ind1+1, ind2)
            else:
                return search(ind1, ind2-1)
            return False
        return search(0, n-1)