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

        first, second = head, prev
        while second:
            fp, sp = first.next, second.next

            first.next = second
            second.next = fp

            first = fp
            second = sp
        
        
