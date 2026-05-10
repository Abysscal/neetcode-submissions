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
        visit = set()
        if not node:
            return None

        def dfs(node):
            if node in oldToNew:
                return oldToNew[node]

            newNode = Node(node.val)
            oldToNew[node] = newNode
            visit.add(node)
            for nei in node.neighbors:
                newNode.neighbors.append(dfs(nei))
            visit.remove(node)

            return newNode

        


        dfs(node)
        return oldToNew[node]