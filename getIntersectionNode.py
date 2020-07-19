# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        la,lb,a,b = 0,0,headA,headB
        while (a or b):
            if (a != None):
                a = a.next
                la += 1
            if (b != None):
                b = b.next
                lb += 1
        if (la > lb):
            l = la- lb
            s = headA
            k = headB
        else:
            l = lb - la
            s = headB
            k = headA
        while (l != 0):
            s= s.next
            l -= 1
        while (s):
            if (s == k):
                return k
            s,k = s.next,k.next
        return None
            
            
            
        