# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pq = [p]
        qq = [q]

        while pq and qq:
            nodep = pq.pop()
            nodeq = qq.pop()

            if nodep and nodeq:
                if nodep.val == nodeq.val:
                    pq.append(nodep.left)
                    pq.append(nodep.right)
                    qq.append(nodeq.left)
                    qq.append(nodeq.right)
                else:
                    return False
            if nodep and not nodeq:
                return False
            if nodeq and not nodep:
                return False

        return True