def singleNonDuplicate(nums: list[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    start = 0
    end = len(nums) - 1

    if nums[0] != nums[1]:
        return nums[0]

    if nums[end] != nums[end - 1]:
        return nums[end]

    while start <= end:
        middle = (start + end) // 2
        if nums[middle] != nums[middle - 1] and nums[middle] != nums[middle + 1]:
            return nums[middle]
        elif (nums[middle] == nums[middle + 1] and middle % 2 == 0) or (nums[middle] == nums[middle - 1] and middle % 2 != 0):
            start = middle + 1
        else:
            end = middle - 1
    return nums[start]


nums = [1,1,3,3,7,7,11,9,9]
print(singleNonDuplicate(nums))