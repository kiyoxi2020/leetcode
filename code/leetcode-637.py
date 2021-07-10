'''
leetcode 637. 二叉树的层平均值

给定一个非空二叉树, 返回一个由每层节点平均值组成的数组。

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        out = []
        stack = [root]
        while(len(stack)>0):
            n = len(stack)
            sum0 = 0
            for _ in range(n):
                t = stack.pop(0)
                sum0 += t.val
                if t.left: stack.append(t.left)
                if t.right: stack.append(t.right)
            out.append(float(sum0)/n)
        return out


