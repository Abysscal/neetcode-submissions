# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        def dfs(preord, inord):
            if not preord or not inord:
                return 
            
            node = TreeNode(preord[0])
            mid = inord.index(node.val)
            
            node.left = dfs(preord[1:mid+1], inord[:mid])
            node.right = dfs(preord[mid+1:], inord[mid+1:])
            
            return node
            
            
            
        
        return dfs(preorder, inorder)