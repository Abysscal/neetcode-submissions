class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        visit = 0
        indeg = [0] * numCourses

        for a,b in prerequisites:
            indeg[b] += 1
            adjlist[a].append(b)

        q = deque()

        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)
    
        while q:
            node = q.popleft()
            visit += 1
            for nei in adjlist[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0 :
                    q.append(nei)

        return numCourses == visit



