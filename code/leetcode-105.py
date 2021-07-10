'''
leetcode 105. 从前序与中序遍历序列构造二叉树

根据一棵树的前序遍历与中序遍历构造二叉树。

注意:
你可以假设树中没有重复的元素。

例如，给出

前序遍历 preorder = [3,9,20,15,7]
中序遍历 inorder = [9,3,15,20,7]
返回如下的二叉树：

    3
   / \
  9  20
    /  \
   15   7

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        dict_in = {}
        n = len(preorder)
        for i in range(n):
            dict_in[inorder[i]] = i
        
        def sort0(pre0, in0, count):
            if len(pre0)==0: return None
            if len(pre0)==1: return TreeNode(pre0[0])
            c = pre0[0]
            i = dict_in[c]-count
            left_in = in0[0:i]
            right_in = in0[i+1:]
            left_pre = pre0[1:1+i]
            right_pre = pre0[1+i:]
            root = TreeNode(c)
            root.left = sort0(left_pre, left_in, count)
            root.right = sort0(right_pre, right_in, count+i+1)
            return root
        
    
        return sort0(preorder, inorder, 0)

