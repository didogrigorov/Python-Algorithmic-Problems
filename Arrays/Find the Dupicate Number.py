from typing import List


def findDuplicate(nums: List[int]) -> int:
    slow, fast = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

nums = [5, 1, 3, 2, 3, 4, 11, 6, 7, 9, 10]
print(findDuplicate(nums))