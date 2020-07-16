# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        n = ListNode('head')
        s = n
        if (l1 == None):
            return l2
        if (l2 == None):
            return l1
        while (l1 and l2):
            if (l1.val > l2.val):
                n.next = l2
                l2 = l2.next
            else:
                n.next = l1
                l1 = l1.next
            n = n.next
        if (l1):
	        n.next = l1
        elif (l2):
	        n.next = l2
        return s.next