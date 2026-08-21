class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
            
        rows, cols = len(grid), len(grid[0])
        direction = [[1,0], [-1,0], [0,1],[0,-1]]
        res = 0
        def bfs(r,c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r,c))

            while queue:
                r,c = queue.popleft()
                for dr,dc in direction:
                    nr = r + dr
                    nc = c + dc
                    if nr not in range(rows) or nc not in range(cols) or grid[nr][nc] == "0":
                        continue
                    queue.append((nr,nc))
                    grid[nr][nc] = "0"



        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    bfs(r,c)
                    res += 1

        return res
