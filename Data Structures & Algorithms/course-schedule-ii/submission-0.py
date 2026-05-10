class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {i:[] for i in range(numCourses)}
        indeg = [0] * numCourses
        res = []

        for a,b in prerequisites:
            indeg[a] += 1
            adjlist[b].append(a)

        def dfs(node):
            res.append(node)
            indeg[node] -= 1
            for nei in adjlist[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    dfs(nei)


        for i in range(numCourses):
            if indeg[i] == 0:
                dfs(i)

        return res if len(res) == numCourses else []