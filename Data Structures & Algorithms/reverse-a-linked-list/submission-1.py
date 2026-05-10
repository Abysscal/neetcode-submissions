# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseList = list()

        while head is not None:
            reverseList.insert(0, head.val)
            head = head.next

        revHead = None
        nxt = None
        for i in reverseList:
            if not revHead:
                revHead = ListNode(i, None)
                nxt = revHead
            else:
                temp = ListNode(i, None)
                nxt.next = temp
                nxt = temp

        return revHead