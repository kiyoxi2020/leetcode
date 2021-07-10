'''
leetcode 99. 恢复二叉搜索树

给你二叉搜索树的根节点 root ，该树中的两个节点被错误地交换。请在不改变其结构的情况下，恢复这棵树。

进阶：使用 O(n) 空间复杂度的解法很容易实现。你能想出一个只使用常数空间的解决方案吗？


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/recover-binary-search-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        node_list = []
        mark = []
        def dfs(h, farther):
            if not h: return
            dfs(h.left, h)
            if len(node_list)>0 and h.val < node_list[-1].val:
                mark.append(len(node_list))
            node_list.append(h)
            dfs(h.right, h)
            return

        dfs(root, None)
        if len(mark) == 1:
            ind = mark[0]
            node_list[ind].val, node_list[ind-1].val = node_list[ind-1].val, node_list[ind].val
        else:
            node_list[mark[0]-1].val, node_list[mark[1]].val = node_list[mark[1]].val, node_list[mark[0]-1].val

        return root
