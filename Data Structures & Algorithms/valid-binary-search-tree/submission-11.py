# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low, upp = float('-inf'), float('inf')

        def dfs(root, low, upp):
            if not root:
                return True
            
            if low < root.val < upp:
                return dfs(root.left, low, root.val) and dfs(root.right, root.val, upp)
            else:
                return False
        
        return dfs(root,low,upp)
                