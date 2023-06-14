# Solution 1 with a HashMap
from typing import List


def findDisappearedNumbers(nums: List[int]) -> List[int]:
    numbers = {}
    result = []

    for num in nums:
        numbers[num] = 1

    for num in range(1, len(nums) + 1):
        if num not in numbers:
            result.append(num)

    return result




nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))