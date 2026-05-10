class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {}
        visit = set()

        for i in range(n):
            adj[i] = []

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adj[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            return True


        if not dfs(0, -1):
            return False
        return  len(visit) == n


        