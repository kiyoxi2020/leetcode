'''
leetcode 234. 回文链表

请判断一个链表是否为回文链表。
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        str0 = []
        while(head):
            str0.append(head.val)
            head = head.next

        return str0==str0[::-1]