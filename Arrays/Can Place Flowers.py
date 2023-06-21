from typing import List


def canPlaceFlowers(flowerbed: List[int], n: int) -> bool:
    empty = 0 if flowerbed[0] else 1

    for f in flowerbed:
        if f:
            n -= int((empty - 1) / 2)  # int division, round toward zero
            empty = 0
        else:
            empty += 1

    n -= (empty) // 2
    return n <= 0

flowerbed = [1,0,0,0,0,0,1]
n = 2
print(canPlaceFlowers(flowerbed, n))