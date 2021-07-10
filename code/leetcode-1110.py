'''
leetcode 1110. 删点成林

给出二叉树的根节点 root，树上每个节点都有一个不同的值。

如果节点值在 to_delete 中出现，我们就把该节点从树上删去，最后得到一个森林（一些不相交的树构成的集合）。

返回森林中的每棵树。你可以按任意顺序组织答案。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/delete-nodes-and-return-forest
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        out = []

        def dfs(h, head, flag):
            if h:
                if h.val in to_delete:
                    if head:
                        if flag: head.left = None
                        else: head.right = None
                    if h.left: dfs(h.left, None, True)
                    if h.right: dfs(h.right, None, False)
                else:
                    if head==None:
                        out.append(h)
                    if h.left: dfs(h.left, h, True)
                    if h.right: dfs(h.right, h, False)
        
        dfs(root, None, True)

        return out

                
            

