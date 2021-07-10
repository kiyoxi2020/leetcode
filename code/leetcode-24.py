
'''
leetcode 24. 两两交换链表中的节点


给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。


'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        out = None
        h1, h0 = None, None
        while(head):
            if h0 and head.next:
                h0.next = head.next
            h0 = head
            head = head.next
            h1 = head
            if head:
                head = head.next
            else:
                if out: return out
                else: return h0
            h1.next = h0
            h0.next = head
            if not out: out = h1
        
        return out
                