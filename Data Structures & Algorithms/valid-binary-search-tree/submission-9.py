# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        low,upp = -float('inf'), float('inf')
        def bfs(node, low, upp):
            if not node:
                return True
            
            if low < node.val < upp:
                return bfs(node.left, low, node.val) and bfs(node.right, node.val, upp)
            else:
                return False
                




        return bfs(root, low,upp)