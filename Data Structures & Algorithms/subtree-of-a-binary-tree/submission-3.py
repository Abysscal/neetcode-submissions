# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSame(root, subroot):
            if not root and not subroot:
                return True

            if root and subroot and root.val == subroot.val:
                return isSame(root.left, subroot.left) and isSame(root.right, subroot.right)
            else:
                return False

        queue = deque([root])
        res = False
        while queue:
            node = queue.popleft()
            if isSame(node, subRoot):
                res = True
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return res