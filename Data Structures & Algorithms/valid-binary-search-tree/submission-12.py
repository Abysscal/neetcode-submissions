# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, upp = float('-inf'), float('inf')

        def dfs(low, node, upp):
            if not node:
                return True
            
            if low < node.val < upp:
                return dfs(low, node.left, node.val) and dfs(node.val,node.right,upp)
            else:
                return False
        return dfs(low, root, upp)
            