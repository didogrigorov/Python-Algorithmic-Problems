import collections
from typing import List


def totalFruit(fruits: List[int]) -> int:
    counter = collections.defaultdict(int)
    left, result, total = 0, 0, 0

    for right in range(len(fruits)):
        counter[fruits[right]] += 1
        total += 1

        while len(counter) > 2:
            f = fruits[l]
            counter[f] -= 1
            total -= 1

            left += 1

            if not counter[f]:
                counter.pop(f)
        result = max(result, total)

    return result


fruits = [1, 2, 1]
print(totalFruit(fruits))
