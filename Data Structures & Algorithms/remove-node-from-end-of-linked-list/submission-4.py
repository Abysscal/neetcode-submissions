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
            length += 1
            cur = cur.next

        count = length - n
        node = ListNode()
        node.next = head
        tail = node
        for i in range(count):
            tail = tail.next
        tail.next = tail.next.next
        return node.next
