from typing import Sequence


def smallestDifference(arrayOne: Sequence[int], arrayTwo: Sequence[int]) -> list[int]:
    arrayOne.sort()
    arrayTwo.sort()

    firstIdx = 0
    secondIdx = 0
    smallest_num = float("inf")
    num_pair = []

    while firstIdx < len(arrayOne) and secondIdx < len(arrayTwo):
        first = arrayOne[firstIdx]
        second = arrayTwo[secondIdx]

        if first < second:
            current = abs(first - second)
            firstIdx += 1
        elif second < first:
            current = abs(first - second)
            secondIdx+= 1
        else:
            return [first, second]

        if smallest_num > current:
            smallest_num = current
            num_pair = [first, second]
    return num_pair

arrayone = [-1, 5, 10, 20, 28, 3]
arraytwo = [26, 134, 135, 15, 17]

print(smallestDifference(arrayone, arraytwo))