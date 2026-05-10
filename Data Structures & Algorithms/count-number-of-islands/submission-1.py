class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        islands = 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            if grid[r][c] == "0":
                return
            if r == 2:
                print()

            visit.add((r,c))
            for rdir, cdir in [[-1, 0], [1,0], [0,-1], [0, 1]]:
                newr = r+ rdir
                newc = c+cdir
                if -1 < newr < rows and -1 < newc < cols and grid[newr][newc] == "1" and (newr,newc) not in visit:
                    bfs(newr,newc)


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visit:
                    bfs(r,c)
                    islands += 1


        return islands