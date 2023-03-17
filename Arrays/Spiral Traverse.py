from typing import Sequence


def spiralTraverse(array: Sequence[int]) -> list[int]:
    spiral = []

    startrow, endrow = 0, len(array) - 1
    startcol, endcol = 0, len(array[0]) - 1

    while startrow <= endrow and startcol <= endcol:

        if startrow > endrow or startcol > endcol:
            return

        for col in range(startcol, endcol + 1):
            spiral.append(array[startrow][col])

        for row in range(startrow + 1, endrow + 1):
            spiral.append(array[row][endcol])

        for col in reversed(range(startcol, endcol)):
            if startcol == endcol or startrow == endrow:
                break
            spiral.append(array[endrow][col])

        for row in reversed(range(startrow + 1, endrow)):
            if startcol == endcol or startrow == endrow:
                break
            spiral.append(array[row][startcol])

        startrow += 1
        endrow -= 1
        startcol += 1
        endcol -= 1

    return spiral


array = [
    [1, 2, 3, 4],
    [10, 11, 12, 5],
    [9, 8, 7, 6],
]
print(spiralTraverse(array))