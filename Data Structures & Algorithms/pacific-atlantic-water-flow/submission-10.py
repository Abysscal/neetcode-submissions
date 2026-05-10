class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r,c,visit,prev):
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or heights[r][c] < prev:
                return
            
            visit.add((r,c))
            dfs(r-1,c,visit,heights[r][c])
            dfs(r+1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])


        for c in range(cols):
            dfs(0, c, pac, -1)
            dfs(rows-1, c, atl, -1)

        for r in range(rows):
            dfs(r, 0, pac, -1)
            dfs(r, cols-1, atl, -1)

        res = []
        for r,c in pac:
            if (r,c) in atl:
                res.append([r,c])

        return res
