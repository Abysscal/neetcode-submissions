class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indeg = [0] * numCourses
        adjlist = [[] for i in range(numCourses)]
        finish=0

        for a,b in prerequisites:
            indeg[b] +=1
            adjlist[a].append(b)

        q = deque()
        for i in range(numCourses):
            if indeg[i] == 0:
                q.append(i)

        while q:
            node = q.popleft()
            finish += 1
            for nei in adjlist[node]:
                indeg[nei] -=1
                if indeg[nei] == 0:
                    q.append(nei)
        return finish == numCourses