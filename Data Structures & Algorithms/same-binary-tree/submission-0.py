# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        ql = deque([p])
        qr = deque([q])

        while ql and qr:
            nodel, noder = ql.popleft(), qr.popleft()
            if not nodel and noder:
                return False
            if nodel and not noder:
                return False
            if nodel and noder and nodel.val != noder.val:
                return False

            if nodel:
                ql.extend([nodel.left, nodel.right])
            if noder:
                qr.extend([noder.left, noder.right])

        return True