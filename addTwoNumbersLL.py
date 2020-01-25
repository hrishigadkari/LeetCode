# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        final = current = ListNode(0)
        carry = 0
        
        while l1 or l2 or carry:
            val1, val2 = 0,0
            if l1:
                val1 = l1.val
                l1 = l1.next
            if l2:
                val2 = l2.val
                l2 = l2.next
            total = val1 + val2 + carry
            carry = total // 10
            value = total % 10
            
            current.next = ListNode(value)
            current = current.next
            
        return final.next