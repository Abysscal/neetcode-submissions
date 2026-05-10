class Solution:
    def exist(self, data: List[List[str]], word: str) -> bool:
    
        def dfs(i,j,w):
            
            if w == len(word):
                return True

            if (min(i,j) < 0 or i >= rows or j >= cols or data[i][j] != word[w] or (i,j) in visited):
                return False

            print(data[i][j])
            visited.add((i,j))
            res = (dfs(i-1, j, w+1) or dfs(i+1, j, w+1) or dfs(i, j-1, w+1) or dfs(i,j+1, w+1))
            visited.remove((i,j))
            return res

        visited = set()
        rows = len(data)
        cols = len(data[0])
        for i in range(rows):
            for j in range(cols):
                if dfs(i,j,0):
                    return True

        return False
