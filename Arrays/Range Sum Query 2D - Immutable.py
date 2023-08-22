from typing import List
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.summat =[[0] * (COLS + 1) for r in range(ROWS + 1)]

        for r in range(ROWS):
            prefix = 0
            for c in range(COLS):
                prefix += matrix[r][c]
                above = self.summat[r][c + 1]
                self.summat[r + 1][c + 1] = prefix + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1 + 1, col1 + 1, row2 + 1, col2 + 1

        bottomright = self.summat[row2][col2]
        above = self.summat[row1-1][col2]
        left = self.summat[row2][col1-1]
        topleft = self.summat[row1 - 1][col1-1]

        return bottomright - above - left + topleft

matrix = [[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]]

myinst = NumMatrix(matrix)
print(myinst.sumRegion(2, 1, 4, 3))