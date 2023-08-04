import collections
from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rows = collections.defaultdict(set)
    cols = collections.defaultdict(set)
    squares = collections.defaultdict(set)

    for row in range(9):
        for col in range(9):
            if board[row][col] == ".":
                continue
            if board[row][col] in rows[row] or board[row][col] in cols[col] or board[row][col] in squares[(row //3, col //3)]:
                return False
            cols[col].add(board[row][col])
            rows[row].add(board[row][col])
            squares[(row // 3, col // 3)].add(board[row][col])

    return True

board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(board))
