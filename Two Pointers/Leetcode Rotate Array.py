from typing import List


def rotate(nums: List[int], k: int):
    k = k % len(nums)

    left = 0
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left = 0
    right = k - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    left = k
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums

nums = [1,2,3,4,5,6,7]
k = 3

print(rotate(nums, k))