"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]
            if not node:
                return

            newNode = Node(node.val)
            oldToNew[node] = newNode
            for nei in node.neighbors:
                if nei not in oldToNew:
                    dfs(nei)
                oldToNew[node].neighbors.append(oldToNew[nei])
            


        dfs(node)
        return oldToNew[node] if node else None