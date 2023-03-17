class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        isDecreasing = False
        isIncreasing = False

        if len(nums) <= 2:
            return True

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue

            if nums[i] < nums[i + 1]:
                isIncreasing = True

            if nums[i] > nums[i + 1]:
                isDecreasing = True

        if isDecreasing and isIncreasing:
            return False
        elif isDecreasing == False and isIncreasing == False:
            return True
        else:
            return isDecreasing or isIncreasing