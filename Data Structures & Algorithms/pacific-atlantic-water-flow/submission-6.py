class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()
        res = []

        def dfs(r, c, visit, prevHeight):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or heights[r][c] < prevHeight:
                return

            visit.add((r, c))

            dfs(r - 1, c, visit, heights[r][c])
            dfs(r + 1, c, visit, heights[r][c])
            dfs(r, c - 1, visit, heights[r][c])
            dfs(r, c + 1, visit, heights[r][c])

        for r in range(rows):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        for row in range(rows):
            for col in range(cols):
                if (row,col) in pac and (row,col) in atl:
                    res.append([row,col])
        return res