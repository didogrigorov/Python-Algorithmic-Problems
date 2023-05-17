from typing import List


def numSubseq(nums: List[int], target: int) -> int:
    nums.sort()
    result = 0
    mod = (10 ** 9 + 7)

    right = len(nums) - 1

    for i, left in enumerate(nums):
        while (left + nums[right]) > target and i <= right:
            right -= 1

        if i <= right:
            result += (2**(right-i))
            result %= mod

    return result



nums = [3,5,6,7]
target = 9
print(numSubseq(nums,target))