# https://neetcode.io/problems/valid-sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from functools import lru_cache

        @lru_cache(maxsize=9)
        def validRow(y):
            found = []
            for i in board[y]:
                if i in found and i != ".":
                    return False
                else:
                    found.append(i)
            return True

        @lru_cache(maxsize=9)
        def validColumn(x):
            found = []
            for y in range(len(board)):
                if board[y][x] in found and board[y][x] != ".":
                    print("invalid column", found, board[y][x])
                    return False
                else:
                    found.append(board[y][x])
            return True
        
        grids = {}
        for y in range(len(board)):
            for x in range(len(board[y])):
                if board[y][x] != ".":
                    if not validRow(y) or not validColumn(x):
                        print("not valid or")
                        return False
                    if x <= 2:
                        gridY = 0
                    elif x > 2 and  x <=5:
                        gridY = 1
                    elif x > 5:
                        gridY = 2

                    if y <= 2:
                        gridX = 0
                    elif y > 2 and y <=5:
                        gridX = 1
                    elif y > 5:
                        gridX = 2
                    
                    gridKey = int(str(gridY)+str(gridX))

                    if gridKey not in grids:
                        grids[gridKey] = []
                    
                    if board[y][x] in grids[gridKey] and board[y][x] != ".":
                        print("grids", gridKey, grids[gridKey], y, x, board[y][x])
                        return False
                    else:
                        grids[gridKey].append(board[y][x])        
        
        return True
