'''
leetcode 160. 相交链表

给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        dict0 = set()
        while(headA or headB):
            if headA:
                if headA in dict0: return headA
                else: dict0.add(headA)
                headA = headA.next
            if headB:
                if headB in dict0: return headB
                else: dict0.add(headB)
                headB = headB.next

        return None