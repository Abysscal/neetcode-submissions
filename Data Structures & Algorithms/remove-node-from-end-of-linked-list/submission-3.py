# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length =0

        cur = head
        while cur:
            cur = cur.next
            length += 1
        
        cur = head
        toremove = length-n 
        if toremove == 0:
            return head.next

        for i in range(length):
            if (i+1) == toremove:
                cur.next = cur.next.next
                break
            cur = cur.next

        return head
