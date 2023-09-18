from typing import List


def shipWithinDays(weights: List[int], days: int) -> int:
    l, r = max(weights), sum(weights)
    res = r

    def can_ship(cap):
        ships, current_cap = 1, cap

        for w in weights:
            if current_cap - w < 0:
                ships += 1
                current_cap = cap
            current_cap -= w
        return ships <= days

    while l <= r:
        cap = (l + r) // 2

        if can_ship(cap):
            res = min(res, cap)
            r = cap - 1
        else:
            l = cap + 1
    return res

weights = [3,2,2,4,1,4]
days = 3
print(shipWithinDays(weights, days))