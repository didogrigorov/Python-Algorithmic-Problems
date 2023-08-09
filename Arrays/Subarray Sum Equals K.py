from typing import List


def subarraySum(nums: List[int], k: int) -> int:
    res = 0
    current_sum = 0
    prefix_sum = {0 : 1}

    for n in nums:
        current_sum += n
        diff = current_sum - k

        res += prefix_sum.get(diff, 0)
        prefix_sum[current_sum] = 1 + prefix_sum.get(current_sum, 0)

    return res

nums = [1,1,1]
print(subarraySum(nums, 2))