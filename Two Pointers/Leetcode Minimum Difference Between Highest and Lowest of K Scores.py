from typing import List
def minimumDifference(nums: List[int], k: int) -> int:
    nums.sort()

    left = 0
    right = k - 1
    result = float("inf")

    while right < len(nums):
        result = min(result, nums[right] - nums[left])
        right += 1
        left += 1

    return result