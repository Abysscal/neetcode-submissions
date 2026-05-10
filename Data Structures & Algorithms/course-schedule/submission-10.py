class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjlist = {i:[] for i in range(numCourses)}
        visit = set()

        for a,b in prerequisites:
            adjlist[a].append(b)
        
        print(adjlist.items())

        def dfs(node):
            if not adjlist[node]:
                return True
            if node in visit:
                return False
            
            visit.add(node)
            print("visited:", node)
            for nei in adjlist[node]:
                print("nei:", nei)
                if not dfs(nei):
                    return False
            visit.remove(node)
            adjlist[node] = []
            print("removing adjlist", adjlist)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True

        
