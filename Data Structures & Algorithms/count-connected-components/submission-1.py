class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0
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

        def bfs(start, parent, values):
            queue = values
            visit.add(start)
            while queue:
                node = queue.pop(0)
                if node not in visit:
                    visit.add(node)
                    queue = queue + adjList[node]


        numberOfComponents = 0
        visit = set()
        for i in range(n):
            if i not in visit:
                bfs(i, -1, adjList[i])
                numberOfComponents += 1
            else:
                continue
        return numberOfComponents
