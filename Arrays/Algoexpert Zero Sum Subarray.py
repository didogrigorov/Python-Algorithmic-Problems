def zeroSumSubarray(nums):
    # Write your code here.
    summed_nums = set([0])
    current = 0

    for num in nums:
        current += num

        if current in summed_nums:
            return True

        summed_nums.add(current)

    return False

# Second version of the problem
def zeroSumSubarray(nums):
    sums = set()
    current_sum = 0

    if len(nums) == 0:
        return False
    elif 0 in nums:
        return True
    elif sum(nums) == 0:
        return True


    for num in nums:
        current_sum += num

        if current_sum in sums:
            return True

        sums.add(current_sum)

    return False