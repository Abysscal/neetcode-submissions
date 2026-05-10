class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjlist = {id:[] for id in range(n)}
        visit = set()

        if len(edges) > (n-1) :
            return False

        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return False
            
            visit.add(node)
            for nei in adjlist[node]:
                if nei != prev:
                    if not dfs(nei, node):
                        return False
            return True
    

        return dfs(0, -1) and len(visit) == n