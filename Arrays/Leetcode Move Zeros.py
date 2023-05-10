from typing import List


def moveZeroes(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    left = 0

    for right in range(len(nums)):
        if nums[right]:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1

    return nums


nums = [0,1,0,3,12]
print(moveZeroes(nums))