# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cur = head
        size = 0
        while cur:
            cur = cur.next
            size += 1

        toRemove = size-n
        if toRemove == 0:
            return head.next

        cur = head
        for i in range(size-1):
            if (i+1) == toRemove:
                cur.next = cur.next.next
                break
            cur = cur.next
        return head