class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        adj = {i:[] for i in range(n)}

        res = 0

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        def dfs(node, prev):
            if node in visit:
                return

            visit.add(node)
            for nei in adj[node]:
                if nei != prev:
                    dfs(nei, node)


        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                res += 1

        return res