# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

    # O(n/2)
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next
        slow.next = None

        # reverse
        prev, nxt = None, None
        #O(n)
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        first, second = head, prev

        #O(n/2)
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1

            first = temp1
            second = temp2

