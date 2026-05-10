class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        for a,b in prerequisites:
            adjList[a].append(b)
        visit = set()

        def dfs(node):
            if not adjList[node]:
                return True
            if node in visit:
                return False

            visit.add(node)
            for edge in adjList[node]:
                if not dfs(edge):
                    return False
                adjList[node].remove(edge)
                visit.remove(node)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True