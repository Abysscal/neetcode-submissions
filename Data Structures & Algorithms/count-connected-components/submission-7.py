class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = {id:[] for id in range(n)}
        visit = set()
        components = 0

        for a,b in edges:
            adjList[a].append(b)
            adjList[b].append(a)

        def dfs(node, prev):
            if node in visit:
                return False

            visit.add(node)
            for edge in adjList[node]:
                if edge != prev:
                    dfs(edge, node)

            return True

        for i in range(n):
            if i not in visit:
                dfs(i, -1)
                components+= 1

        return components