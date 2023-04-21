from typing import List


def getConcatenation(self, nums: List[int]) -> List[int]:
    nums_len = len(nums)
    ans = nums + [0] * nums_len

    for i in range(nums_len):
        ans[i + nums_len] = nums[i]

    return ans

# Neetcode Solution
# def getConcatenation(self, nums: List[int]) -> List[int]:
#     ans = []
#     for i in range(2):
#         for n in nums:
#             ans.append(n)
#     return ans
