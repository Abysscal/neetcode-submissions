# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')

        def dfs(node):
            nonlocal res
            if not node:
                return 0
            
            leftMax = dfs(node.left)
            leftMax = max(leftMax, 0)
            rightMax = dfs(node.right)
            rightMax = max(rightMax, 0)
            pathsum = leftMax + rightMax + node.val
            res = max(pathsum, res)

            return max(leftMax, rightMax) + node.val



        dfs(root)
        return res