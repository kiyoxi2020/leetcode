'''
leetcode 144. 二叉树的前序遍历

给你二叉树的根节点 root ，返回它节点值的 前序 遍历。

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []
        stack = []
        while(1):
            if not root:
                if len(stack)==0: break
                root = stack.pop(0)
            out.append(root.val)
            if root.right:
                stack.insert(0, root.right)
            if root.left:
                root = root.left
            else: 
                root = None
            if not root and len(stack)==0:
                break

        return out


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        out = []

        def dfs(h):
            if not h: return
            out.append(h.val)
            dfs(h.left)
            dfs(h.right)
            return
        
        dfs(root)
        return out