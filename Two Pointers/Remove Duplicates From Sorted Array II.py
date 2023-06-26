from typing import List
def removeDuplicates(nums: List[int]) -> int:
    left = 0
    right = 0

    while right < len(nums):
        count = 1
        while right + 1 < len(nums) and nums[right] == nums[right + 1]:
            right += 1
            count += 1

        for i in range(min(2, count)):
            nums[left] = nums[right]
            left += 1

        right += 1

    return left

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))