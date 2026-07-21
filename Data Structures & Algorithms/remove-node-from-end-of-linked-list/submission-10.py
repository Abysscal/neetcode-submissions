# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        pre = ListNode()
        pre.next = head

        count = head
        size = 0
        while count:
            size += 1
            count = count.next

        pos = size - n

        prev = pre
        curr = head
        for i in range(size):
            if i == pos:
                prev.next = curr.next
                break
            prev = curr
            curr = curr.next
        return pre.next
