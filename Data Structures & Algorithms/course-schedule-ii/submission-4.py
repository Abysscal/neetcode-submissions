class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {c:[] for c in range(numCourses)}
        indeg = {c:0 for c in range(numCourses)}
        res = []

        for a,b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1

        q = deque([])
        for i in indeg:
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            res.append(node)
            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        res.reverse()
        return res if len(res) == numCourses else []