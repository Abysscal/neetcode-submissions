# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []
        res = []
        queue.append(root)

        while queue:
            qlen = len(queue)
            level = []
            for i in range(qlen):
                node = queue.pop(0)
                if node and node.val is not None:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
            # print("level:",level)

        # print(res)
        return res