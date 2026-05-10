class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
            # num courses is the number of nodes, 
        adj = [[] for i in range(numCourses)]
        #mapping for adj list
        for req in prerequisites:
            adj[req[1]].append(req[0])
        
        visited = [False] * numCourses

        def dfs(node):
            if visited[node] :
                return False
            if adj[node] == []:
                return True
            
            visited[node] = True
            for x in adj[node]:
                if not dfs(x): return False
            visited[node] = False
            adj[node] = []
            return True
            
            
        
        for i in range(numCourses):
            if not dfs(i): return False
        return True