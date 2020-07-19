# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        w,r=head,head
        while (r and r.next):
            w = w.next
            r = r.next.next
        a = None
        while(w):
            b = w
            w = w.next
            b.next = a
            a = b
        while head and a:
            if (head.val != a.val):
                return False
            head = head.next
            a = a.next
        return True
        
            