def searchInsert(self, nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        midnum = (start + end) // 2

        if nums[midnum] == target:
            return midnum
        elif target > nums[midnum]:
            start = midnum + 1
        else:
            end = midnum - 1

    return start