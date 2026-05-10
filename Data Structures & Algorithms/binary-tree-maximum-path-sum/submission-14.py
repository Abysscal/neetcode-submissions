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

            left = dfs(node.left)
            leftMax = max(left, 0)
            right = dfs(node.right)
            rightMax = max(right, 0)
            
            sum = node.val + leftMax + rightMax
            res = max(sum, res)
            
            return max(leftMax, rightMax) + node.val
        
        dfs(root)
        return res