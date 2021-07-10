'''
leetcode 543. 二叉树的直径

给定一棵二叉树，你需要计算它的直径长度。一棵二叉树的直径长度是任意两个结点路径长度中的最大值。这条路径可能穿过也可能不穿过根结点。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(h):
            if not h: return -1, 0
            l_depth, l_length = dfs(h.left) 
            r_depth, r_length = dfs(h.right)
            l_depth += 1
            r_depth += 1
            depth = max(l_depth, r_depth)
            length = l_depth+r_depth
            return depth, max(l_length, r_length, length)
        
        depth, length = dfs(root)
        return length

