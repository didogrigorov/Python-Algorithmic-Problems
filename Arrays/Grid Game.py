from typing import List

# Solution 1
def gridGame(grid: List[List[int]]) -> int:
    N = len(grid[0])
    prefix_row1, prefix_row2 = grid[0].copy(), grid[1].copy()

    for i in range(1, N):
        prefix_row1[i] += prefix_row1[i - 1]
        prefix_row2[i] += prefix_row2[i - 1]

    result = float("inf")

    for i in range(N):
        top = prefix_row1[-1] - prefix_row1[i]
        bottom = prefix_row2[i - 1] if i > 0 else 0
        secondRobot = max(top, bottom)
        result = min(result, secondRobot)

    return result

# Solution 2
def gridGame(grid: List[List[int]]) -> int:
    res = float('inf')

    bottom, top = 0, sum(grid[0])

    for a, b in zip(grid[0], grid[1]):
        top -= a
        res = min(res, max(top, bottom))
        bottom += b

    return res

print(gridGame([[2, 5, 4], [1, 5, 1]]))
