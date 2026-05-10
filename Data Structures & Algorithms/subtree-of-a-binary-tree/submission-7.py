# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([root])
        res = False

        def dfs(p,q):
            if not p and not q:
                return True
            
            if p and q and p.val == q.val:
                return dfs(p.left, q.left) and dfs(p.right, q.right)
            else:
                return False

        while queue:
            node = queue.popleft()
            if node and node.val == subRoot.val:
                temp = dfs(node, subRoot)
                if temp:
                    res = temp
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return res