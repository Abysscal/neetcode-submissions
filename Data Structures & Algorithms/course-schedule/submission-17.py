class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = {i:[] for i in range(numCourses)}
        visit = set()

        for a,b in prerequisites:
            adjList[a].append(b)

        def dfs(node):
            if not adjList[node]:
                return True

            if node in visit:
                return False

            visit.add(node)
            for b in adjList[node]:
                if not dfs(b):
                    return False
                adjList[node].remove(b)
            visit.remove(node)


            return True

        for i in range(numCourses):
            if not dfs(i):
                return False

        return True