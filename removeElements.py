# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        extra = ListNode(0)
        extra.next = head
        a = extra
        while (a.next):
            if (a.next.val == val):
                a.next = a.next.next
            else:
                a = a.next
        return extra.next
       