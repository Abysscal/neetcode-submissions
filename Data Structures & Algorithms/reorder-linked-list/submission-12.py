# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        fast, slow = head, head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        midStart = slow.next
        slow.next = None

        # reverse here
        prev, curr = None, midStart

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev
        while second:
            print(first.val)
            print(second.val)
            tmp1 = first.next
            tmp2 = second.next
            first.next = second
            second.next = tmp1
            second = tmp2
            first = tmp1