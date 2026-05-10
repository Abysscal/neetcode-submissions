class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = {i: [] for i in range(n)}

        for edge in edges:
            u, v = edge[0], edge[1]
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(current, parent, values):
            if current in visit:
                return False

            visit.add(current)

            for val in values:
                if val == parent:
                    continue
                if not dfs(val, current, adjList[val]):
                    return False
            return True

        visit = set()
        # exit condition is that its a cycle/ not valid
        if not dfs(0, -1, adjList[0]):
            return False
        if len(visit) != n:
            return False
        
        return True