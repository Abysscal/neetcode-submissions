class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board or not board[0]:
            return False
        rows, cols = len(board), len(board[0])
        gridrows = [set() for _ in range(rows)] 
        gridcols = [set() for _ in range(cols)]
        gridbox = [[set() for _ in range(3)] for _ in range(3)]

        for r in range(rows):
            for c in range(cols):
                if board[r][c] != ".":
                    # check if value is in set, if so return False
                    num = board[r][c]
                    if num in gridrows[r]:
                        print('row',num, r,c)
                        return False

                    # add it to the set
                    gridrows[r].add(num)

                    if num in gridcols[c]:
                        print('col',num, r,c)
                        return False

                    # add it to the set
                    gridcols[c].add(num)

                    # check for the gridbox
                    if num in gridbox[r // 3][c // 3]:
                        print("gridbox" + num, r,c)
                        return False
                    gridbox[r//3][c//3].add(num)
        
        return True