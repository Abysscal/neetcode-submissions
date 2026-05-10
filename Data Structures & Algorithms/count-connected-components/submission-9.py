class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return True

        comp = 0
        adjlist = {i:[] for i in range(n)}
        visit = set()

        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return
            
            visit.add(node)
            for nei in adjlist[node]:
                if nei != node:
                    dfs(nei, node)
            
        

        for i in range(n):
            if i not in visit:
                dfs(i,-1)
                comp +=1
        return comp