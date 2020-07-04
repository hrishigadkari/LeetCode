# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        count,dec = 0,0
        temp = head
        while(temp):
            temp = temp.next
            count += 1
        temp = head
        while(temp):
            dec = dec + (temp.val*pow(2,count-1))
            temp = temp.next
            count -= 1
        return dec