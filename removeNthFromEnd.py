# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        a,b = ListNode(-1),ListNode(-1)
        a.next,b.next = head,head
        if head == None:
            return None
        while(a):
            a = a.next
            if (n == -1):
                b = b.next
            else:
                n -= 1
        b.next = b.next.next
        if (a == None and b.val == -1):
            return head.next
        return head
                
            