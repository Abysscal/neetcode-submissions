class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visit = set()
        maxarea = 0
        directions = [[1,0],[-1,0],[0,-1],[0,1]]

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == 0:
                return 0
            
            visit.add((r,c))
            # print(visit)
            return 1 + dfs(r-1,c) + dfs(r+1,c) + dfs(r,c-1) + dfs(r,c+1)

        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visit:
                    size = dfs(r,c)
                    maxarea = max(size, maxarea)
        
        return maxarea
