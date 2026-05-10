# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prev, curr, nxt = None, head, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        tail = node = ListNode()
        tail.next = prev

        prevNode = None
        for i in range(n):
            prevNode = tail
            tail = tail.next

        # remove node and join

        prevNode.next = tail.next

        prev, curr, nxt = None, node.next, None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev