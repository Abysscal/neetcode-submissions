# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root or root.val == None:
            return ""
        queue = deque([root])
        res = ""
        while queue:
            node = queue.popleft()
            if node:
                res += str(node.val)+","
                if node.left:
                    queue.append(node.left)
                else:
                    queue.append(None)
                if node.right:
                    queue.append(node.right)
                else:
                    queue.append(None)
            else:
                res+= "None,"
        if res[-1] == ',':
            res = res[:-1]
        return str(res)



    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data = data.split(",")
        for i in range(len(data)):
            if data[i] != "None":
                data[i] = int(data[i])
            else:
                data[i] = None
        data = deque(data)
        root = TreeNode(data.popleft())
        queue = deque([root])
        while data:
            node = queue.popleft()
            if data[0]:
                node.left = TreeNode(data.popleft())
                queue.append(node.left)
            else:
                data.popleft()
            if data[0]:
                node.right = TreeNode(data.popleft())
                queue.append(node.right)
            else:
                data.popleft()

        return root