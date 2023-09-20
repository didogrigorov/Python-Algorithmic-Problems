from typing import List


def minimizeMax(nums: List[int], p: int) -> int:
    if p == 0: return 0
    nums.sort()

    def isValid(threshold):
        i, count = 0, 0
        while i < len(nums) - 1:
            if abs(nums[i] - nums[i + 1]) <= threshold:
                count += 1
                i += 2
            else:
                i += 1

            if count == p:
                return True
        return False

    l, r = 0, 10 ** 9
    res = 10 ** 9

    while l <= r:
        m = l + ((r - l) // 2)

        if isValid(m):
            res = m
            r = m - 1
        else:
            l = m + 1

    return res
nums = [10,1,2,7,1,3]
p = 2
print(minimizeMax(nums, p))