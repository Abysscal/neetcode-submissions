class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights), len(heights[0])
        pac, atl = set(), set()


        def dfs(r,c, visit, lastHeight):
            if r < 0 or r > ROWS-1 or c < 0 or c > COLS-1 or (r,c) in visit or heights[r][c] < lastHeight:
                return

            visit.add((r,c))
            dfs(r-1, c, visit, heights[r][c])
            dfs(r+1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])


        # start from all edges:
        for c in range(COLS):
            dfs(0,c, pac, heights[0][c])
            dfs(ROWS-1, c, atl, heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac, heights[r][0])
            dfs(r, COLS-1, atl, heights[r][COLS-1])

        result = list()

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in pac and (r,c) in atl:
                    result.append([r,c])

        return result