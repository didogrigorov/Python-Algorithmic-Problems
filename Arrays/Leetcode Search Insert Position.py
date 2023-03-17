def searchInsert(nums: list[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        midnum = (start + end) // 2

        if nums[midnum] == target:
            return midnum
        elif nums[midnum] > target:
            end = midnum - 1
        else:
            start = midnum + 1

    return end + 1