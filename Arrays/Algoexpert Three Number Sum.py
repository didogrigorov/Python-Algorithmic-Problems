from typing import Sequence


def threeNumberSum(array: Sequence[int], targetSum:int) -> list[tuple[int, int, int]]:
    array.sort()
    triplets = []

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            current = array[i] + array[left] + array[right]

            if current == targetSum:
                triplets.append((array[i], array[left], array[right]))
                left += 1
                right -= 1

            elif current < targetSum:
                left += 1
            elif current > targetSum:
                right -= 1

    return triplets




test_array = [12,3,1,2,-6,5,-8,6]
targetSum = 0
print(threeNumberSum(test_array, targetSum))