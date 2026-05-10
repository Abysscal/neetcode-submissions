# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        finalList = None
        curr = None
        finalcurr = None

        while list1 or list2:
            if list1 and list2 and list1.val <= list2.val:
                curr = list1
                list1 = list1.next
            elif list1 and list2 and list2.val < list1.val:
                curr = list2
                list2 = list2.next
            elif list1:
                curr = list1
                list1 = list1.next
            elif list2:
                curr = list2
                list2 = list2.next
            if not finalList:
                finalList = curr
                finalcurr = curr
            else:
                finalcurr.next = curr
                finalcurr = finalcurr.next



        return finalList
