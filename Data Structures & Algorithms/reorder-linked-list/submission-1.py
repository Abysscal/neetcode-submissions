# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next

        # reverse
        prev, nxt = None, None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        tail = node = ListNode()

        while tail and prev:
            tail.next = head
            head = head.next
            tail = tail.next

            tail.next = prev
            prev = prev.next
            tail = tail.next

        tail.next = head
        tail.next.next = None

        print(node.next)