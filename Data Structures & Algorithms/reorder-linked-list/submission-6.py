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
        slow.next = None

        cur = mid
        prev, nxt = None, None
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        cur = head
        first, second = cur, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next =tmp1

            first = tmp1
            second = tmp2