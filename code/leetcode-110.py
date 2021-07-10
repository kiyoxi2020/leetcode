'''
leetcode 110. 平衡二叉树

给定一个二叉树，判断它是否是高度平衡的二叉树。

本题中，一棵高度平衡二叉树定义为：

一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1 。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def dfs(h):
            if not h: return 0, True
            l, flag1 = dfs(h.left)
            r, flag2 = dfs(h.right)
            l, r = l+1, r+1
            if (not flag1) or (not flag2) or abs(l-r)>1: 
                return max(l, r), False
            else: return max(l, r), True

        depth, flag = dfs(root)
        return flag
            
