# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        cur = head
        length = 0

        while cur:
            cur = cur.next
            length += 1
        removepos = length-n
        if removepos == 0:
            return head.next

        cur = head
        for i in range(removepos):
            if (i+1) == removepos:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head
            