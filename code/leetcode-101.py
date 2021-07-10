
'''
leetcode 101. 对称二叉树

给定一个二叉树，检查它是否是镜像对称的。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(h1, h2):
            if h1 and h2:
                if h1.val!=h2.val: return False
                else:
                    return dfs(h1.left, h2.right) and dfs(h1.right, h2.left)
            elif not h1 and not h2:
                return True
            else:
                return False
        
        return dfs(root.left, root.right)