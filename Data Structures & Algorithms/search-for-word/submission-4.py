class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        word = list(word)
        visit = set()
        curr = 0
        rows, cols = len(board), len(board[0])
        def dfs(r,c,curr):
            if curr == len(word) :
                return True
            if r not in range(rows) or c not in range(cols) or (r,c) in visit or board[r][c] != word[curr]:
                return False
            visit.add((r,c))
            res = (dfs(r+1,c,curr+1) or
            dfs(r-1,c,curr+1) or
            dfs(r,c+1,curr+1) or
            dfs(r,c-1,curr+1))
            visit.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                visit = set()
                if board[r][c] == word[curr]:
                    if dfs(r,c,curr):
                        return True

        return False
