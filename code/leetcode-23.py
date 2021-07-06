# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
'''
leetcode 23. 合并K个升序链表

给你一个链表数组，每个链表都已经按升序排列。

请你将所有链表合并到一个升序链表中，返回合并后的链表。

 
'''
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        def merge(list1, list2):
            head = ListNode()
            head0 = head
            while(list1 or list2):
                if (list1 and list2 and list1.val < list2.val) or (list1 and not list2):
                    head.next = list1
                    list1 = list1.next
                else:
                    head.next = list2
                    list2 = list2.next
                head = head.next
            return head0.next

        if not lists:
            return None
        while(1):
            list0 = []
            n = len(lists)
            i = 0
            while(i<n):
                if i+1 < n:
                    t = merge(lists[i],lists[i+1])
                    list0.append(t)
                else:
                    list0.append(lists[i])
                i+=2
            if len(list0) == 1:
                break
            lists=list0

        return list0[0]
