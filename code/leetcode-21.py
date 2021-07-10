
'''
leetcode 21. 合并两个有序链表

将两个升序链表合并为一个新的 升序 链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

'''
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        last, head = None, None
        while(l1 or l2):
            t = None
            if l1 and l2:
                if l1.val < l2.val:
                    t = l1
                    l1 = l1.next
                else:
                    t = l2
                    l2 = l2.next
            elif l1:
                t = l1
                l1 = l1.next
            else:
                t = l2
                l2 = l2.next
            if not head:
                head = t
                last = t
            else:
                last.next = t
                last = t
        return head


                    
