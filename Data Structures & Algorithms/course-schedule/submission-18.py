class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adj = [[] for i in range(numCourses)]

        for a,b in prerequisites:
            indeg[b] += 1
            adj[a].append(b)

        q = deque()
        for deg in range(numCourses):
            if indeg[deg] == 0:
                q.append(deg)

        res = 0
        while q:
            node = q.popleft()
            res += 1

            for b in adj[node]:
                indeg[b] -= 1
                if indeg[b] == 0:
                    q.append(b)


        if res == numCourses:
            return True
        else:
            return False
