# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 0 1 2 3 4
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        mid = slow.next
        slow.next = None

        prev, nxt = None, None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt

        first, second = head, prev

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1

            first = tmp1
            second = tmp2
        


