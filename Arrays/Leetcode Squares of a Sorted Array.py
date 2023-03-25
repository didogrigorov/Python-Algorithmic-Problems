def sortedSquares(nums):
    n = len(nums)
    result = [0] * n
    j = -1
    left = 0
    right = n - 1

    for i in range(n):

        if abs(nums[left]) < abs(nums[right]):
            squared = nums[right]
            right -= 1
        else:
            squared = nums[left]
            left += 1

        result[j] = squared * squared
        j -= 1

    return result


nums = [-3, -2, -1, 4, 5, 6]
print(sortedSquares(nums))