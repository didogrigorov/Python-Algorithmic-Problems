from typing import List
def minSubArrayLen(target: int, nums: List[int]) -> int:
    left, total = 0, 0
    res = float("inf")

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            res = min(res, r - left + 1)
            total -= nums[left]
            left += 1

    return 0 if res == float("inf") else res


nums = [2,3,1,2,4,3]
target = 7
print(minSubArrayLen(target, nums))