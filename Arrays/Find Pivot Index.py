from typing import List


def pivotIndex(nums: List[int]) -> int:
    total = sum(nums)

    left_sum = 0

    for i in range(len(nums)):
        right_sum = total - nums[i] - left_sum

        if left_sum == right_sum:
            return i

        left_sum += nums[i]

    return -1

nums = [1,7,3,6,5,6]
print(pivotIndex(nums))