from typing import List


def numRescueBoats(people: List[int], limit: int) -> int:
    people.sort()
    result = 0

    l, r = 0, len(people) - 1

    while l <= r:
        remaining = limit - people[r]
        r -= 1
        result += 1
        if l <= r and remaining >= people[l]:
            l += 1

    return result


people = [3, 2, 2, 1]
limit = 3
print(numRescueBoats(people, limit))
