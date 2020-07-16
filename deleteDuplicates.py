# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if (head == None):
            return head            
        s,v = head, head.next
        while(v):
            if(head.val == v.val):
                head.next = v.next
                v.next = None
            else:
                head = head.next
            v = head.next
        return s
        