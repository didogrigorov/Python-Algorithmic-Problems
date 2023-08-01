from typing import List


def maxFrequency(nums: List[int], k: int) -> int:
    nums.sort()

    l, r = 0, 0
    res, total = 0, 0

    while r < len(nums):
        total += nums[r]

        while nums[r] * (r - l + 1) > total + k:
            total -= nums[l]
            l += 1

        res = max(res, r - l + 1)
        r += 1

    return res

print(maxFrequency([1, 2, 3, 4], 3))