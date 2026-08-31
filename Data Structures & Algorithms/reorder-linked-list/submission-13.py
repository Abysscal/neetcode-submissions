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

        prev,nxt = None, None
        while mid:
            nxt = mid.next
            mid.next = prev
            prev = mid
            mid = nxt
        
        first, second = head, prev

        while second:
            n1,n2 = first.next, second.next
            first.next = second
            second.next = n1

            first = n1
            second = n2
        
        