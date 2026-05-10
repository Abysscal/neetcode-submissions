# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return isBST( root, float('-inf'), float('inf'))



def isBST( node, minVal, maxVal):
    if node is None or node.val is None:
        return True

    if node.val < minVal or node.val > maxVal:
        return False

    return (isBST(node.left, minVal, node.val - 1) and isBST(node.right, node.val + 1, maxVal))