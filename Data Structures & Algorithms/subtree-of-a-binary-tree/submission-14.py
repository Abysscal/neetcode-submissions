# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isSub(l, r):
            if not l and not r:
                return True
            if not l or not r or l.val != r.val:
                return False

            return isSub(l.left, r.left) and isSub(l.right, r.right)

        if not subRoot:
            return True

        if not root and subRoot:
            return False

        q = deque([root])

        while q:
            node = q.popleft()
            if node:
                if node.val == subRoot.val:
                    if isSub(node, subRoot):
                        return True
                q.append(node.left)
                q.append(node.right)
        return False
