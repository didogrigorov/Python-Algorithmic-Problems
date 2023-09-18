from typing import List


def successfulPairs(spells: List[int], potions: List[int], success: int) -> List[int]:
    potions.sort()
    res = []

    for s in spells:
        l, r = 0, len(potions) - 1
        idx = len(potions)

        while l <= r:
            m = (l + r) // 2

            if s * potions[m] >= success:
                r = m - 1
                idx = m
            else:
                l = m + 1

        res.append(len(potions) - idx)

    return res
spells = [5, 1, 3]
potions = [1,2,2,4,5]
success = 7
print(successfulPairs(spells, potions, success))