# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = head
        size = 0
        while count:
            size += 1
            count = count.next

        pos = size - n
        if pos == 0 :
            return head.next

        curr = head
        for i in range(size):
            if (i+1) == pos:
                curr.next = curr.next.next
                break
            curr = curr.next

        return head