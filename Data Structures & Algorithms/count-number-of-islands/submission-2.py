class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit=set()
        islands = 0

        rows, cols = len(grid), len(grid[0])

        def bfs(r,c):
            q = deque()
            visit.add((r,c))
            q.append((r,c))
            directions = [[-1, 0], [1,0], [0,-1], [0, 1]]
            while q:
                row,col = q.popleft()
                for dr, dc in directions:
                    r = row+ dr
                    c = col+ dc
                    if -1 < r < rows and -1 < c < cols and grid[r][c] == "1" and (r,c) not in visit:
                        q.append((r,c))
                        visit.add((r,c))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    bfs(row,col)
                    islands += 1


        return islands