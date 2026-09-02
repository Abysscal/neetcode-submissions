class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {i:[] for i in range(numCourses)}
        indeg = [0] * numCourses

        for a,b in prerequisites:
            adj[a].append(b)
            indeg[b] += 1
        
        q = deque([])

        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)
        
        res = 0 
        while q:
            node = q.popleft()
            res += 1

            for nei in adj[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)

        return True if res == numCourses else False

