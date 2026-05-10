# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        upp, low = float('inf'), -float('inf')

        def dfs(node, low, upp):
            if not node:
                return True


            if low < node.val < upp:
                return dfs(node.left, low, node.val) and dfs(node.right, node.val, upp)
            else:
                return False

        return dfs(root, low, upp)