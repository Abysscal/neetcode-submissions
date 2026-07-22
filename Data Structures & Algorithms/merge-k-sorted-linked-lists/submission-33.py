# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        counter = 0

        for i in lists:
            heapq.heappush(heap, (i.val, counter, i))
            counter += 1


        # Step 1: Initialize heap with first nodes

        # Step 2: Build result
        result = dummy = ListNode()

        while heap:
            # Step 3: Pop, add to result, push next node
            nodeVal, count, node = heapq.heappop(heap)
            result.next = node
            node = node.next
            if node:
                heapq.heappush(heap, (node.val, counter, node))
                counter += 1
            result = result.next
        return dummy.next