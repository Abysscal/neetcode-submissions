class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = set()
        islands = 0
        rows, cols = len(grid), len(grid[0])
        directions = [[-1,0],[1,0],[0,-1],[0,1]]

        def dfs(r,c):
            q = deque()
            q.append((r,c))

            while q:
                r,c = q.popleft()
                visit.add((r,c))
                for dr,dc in directions:
                    newr = r + dr
                    newc = c + dc
                    if newr in range(rows) and newc in range(cols) and grid[newr][newc] == "1" and (newr,newc) not in visit:
                        q.append((newr,newc))
                        visit.add((newr,newc))


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visit:
                    dfs(row,col)
                    islands +=1
        return islands