class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjlist = {id:[] for id in range(numCourses)}
        indeg = [0] * numCourses
        finish =0 
        res = []

        for a,b in prerequisites:
            indeg[b] += 1
            adjlist[a].append(b)

        q = deque()
        for n in range(numCourses):
            if indeg[n] == 0:
                q.append(n)

        while q:
            node = q.popleft()
            res.append(node)
            finish += 1
            for nei in adjlist[node]:
                indeg[nei] -= 1
                if indeg[nei] == 0:
                    q.append(nei)
            
        return res[::-1] if finish == numCourses else []