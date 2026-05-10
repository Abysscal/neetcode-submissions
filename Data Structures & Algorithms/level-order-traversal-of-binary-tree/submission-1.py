# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelOrder = []
        queue = deque([root])

        while queue:
            tmpList = []
            for i in range(len(queue)):
                node = queue.popleft()
                if node:
                    tmpList.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if tmpList:
                levelOrder.append(tmpList)

        return levelOrder