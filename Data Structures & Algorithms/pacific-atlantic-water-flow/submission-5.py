class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        rows, cols = len(heights), len(heights[0])
        res = []

        def bfs(row,col):
            visit = set()
            q = deque()
            q.append((row, col))
            directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]
            pacific = False
            atlantic = False
            while q:
                r,c = q.popleft()
                visit.add((r,c))
                for dr, dc in directions:
                    newr = r +dr
                    newc = c+dc
                    if newr in range(rows) and newc in range(cols) and (newr, newc) not in visit and heights[newr][newc] <= heights[r][c]:
                        q.append((newr,newc))
                        visit.add((r,c))

                if r == 0 or c == 0:
                    pacific = True
                if r == rows-1 or c == cols-1:
                    atlantic = True
            return pacific and atlantic


        for row in range(rows):
            for col in range(cols):
                if  bfs(row, col):
                    res.append([row, col])

        return res