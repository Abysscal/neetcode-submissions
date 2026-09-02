class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or grid[r][c] == "0":
                return
            
            visit.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        

        rows, cols = len(grid), len(grid[0])
        visit = set()
        res =0


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    dfs(r,c)
                    res += 1

        return res


        
