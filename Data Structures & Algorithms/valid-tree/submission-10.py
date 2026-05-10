class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adjList = dict()

        for i in range(n):
            adjList[i] = []

        for edge in edges:
            u, v = edge[0], edge[1]
            adjList[u].append(v)
            adjList[v].append(u)

        def dfs(current, parent, values, visited):
            visited.add(current)

            for val in values:
                    if val not in visited:
                        dfs(val, current, adjList[val], visited)
                    elif val != parent:
                        return True

            return False


        for key, value in adjList.items():
            visit = set()
            # exit condition is that its a cycle/ not valid
            if dfs(key, -1, value, visit):
                return False
            if len(visit) != n:
                return False

        return True