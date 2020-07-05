class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        a = None
        while(head):
            b = head
            head = head.next
            b.next = a
            a = b
        return a