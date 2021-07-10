'''
leetcode 206. 反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        last = None
        while(head):
            head0 = head
            head = head.next
            head0.next = last
            last = head0
        return last
            