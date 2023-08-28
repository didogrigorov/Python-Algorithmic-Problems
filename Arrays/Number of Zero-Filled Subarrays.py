class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        result, counter = 0, 0

        for i in range(len(nums)):
            if nums[i] == 0:
                counter += 1
            else:
                counter = 0
            result += counter

        return result