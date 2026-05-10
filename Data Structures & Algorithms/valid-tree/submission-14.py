class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (n-1)!= len(edges):
            return False

        adjList = {id:[] for id in range(n)}
        visit = set()

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for edge in adjList[node]:
                if edge != prev:
                    if not dfs(edge, node):
                        return False

            return True

        return dfs(0, -1) and len(visit) == n