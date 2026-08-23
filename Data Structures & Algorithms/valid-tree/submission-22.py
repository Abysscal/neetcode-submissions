class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if (len(edges)+1) != n:
            return False

        adj = {i:[] for i in range(n)}
        res = 0
        visit = set()

        for a,b in edges:
            adj[a].append(b)
            adj[b].append(a)


        def dfs(node, prev):
            nonlocal res
            if node in visit:
                return False

            visit.add(node)
            res += 1
            for b in adj[node]:
                if b != prev:
                    if not dfs(b, node):
                        return False

            return True

        dfs(0,-1)
        return res == n