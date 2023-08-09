from typing import List


def leastBricks(wall: List[List[int]]) -> int:
    count_gap = { 0 : 0} # pos : brick gaps

    for r in wall:
        total = 0
        for b in r[: -1]:
            total += b
            count_gap[total] = 1 + count_gap.get(total, 0)

    return len(wall) - max(count_gap.values())



wall = [[1, 2, 2, 1],
        [3, 1, 2],
        [1, 3, 2],
        [2, 4],
        [3, 1, 2],
        [1, 3, 1, 1]]
print(leastBricks(wall))
