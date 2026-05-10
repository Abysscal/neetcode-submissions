class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjlist = {id:[] for id in range(n)}
        comps = 0
        visit = set()

        for a,b in edges:
            adjlist[a].append(b)
            adjlist[b].append(a)
        
        def dfs(node, prev):
            if node in visit:
                return

            visit.add(node)
            for nei in adjlist[node]:
                if prev != nei:
                    dfs(nei, node)
            


        
        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                comps += 1
        
        return comps

        