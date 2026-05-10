class Solution:
    def numIslands(self, data: List[List[str]]) -> int:
        def dfs(r,c):
            if min(r,c) < 0 or r >= rows or c >= cols or (r,c) in visited or data[r][c] == "0":
                return

            visited.add((r,c))
            dfs(r-1,c)
            dfs(r+1,c)
            dfs(r,c-1)
            dfs(r,c+1)        
        
        visited = set()

        rows = len(data)
        cols = len(data[0])
        res = 0
        for r in range(rows):
            for c in range(cols):
                if data[r][c] == "1" and (r,c) not in visited:
                    dfs(r,c)
                    res += 1

        return res