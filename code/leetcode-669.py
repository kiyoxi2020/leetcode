'''
leetcode 669. 修剪二叉搜索树


给你二叉搜索树的根节点 root ，同时给定最小边界low 和最大边界 high。通过修剪二叉搜索树，使得所有节点的值在[low, high]中。修剪树不应该改变保留在树中的元素的相对结构（即，如果没有被移除，原有的父代子代关系都应当保留）。 可以证明，存在唯一的答案。

所以结果应当返回修剪好的二叉搜索树的新的根节点。注意，根节点可能会根据给定的边界发生改变。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/trim-a-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def trimBST(self, root, low, high):
        """
        :type root: TreeNode
        :type low: int
        :type high: int
        :rtype: TreeNode
        """

        def dfs(h, farther):
            if not h: return None
            if h.val < low:
                if h.right: t = dfs(h.right, farther)
                else: t = None
                if farther: farther.left = t
                return t
            elif h.val > high:
                if h.left: t = dfs(h.left, farther)
                else: t = None
                if farther: farther.right = t
                return t
            else:
                h.left = dfs(h.left, h)
                h.right = dfs(h.right, h)
                return h

                  
        return dfs(root, None)  

                    
