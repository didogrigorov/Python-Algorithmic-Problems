def twoSum(nums, target):

    checked_nums = {}

    for index, number in enumerate(nums):
        addition = target - nums[index]

        element = checked_nums.get(addition)

        if element is not None:
            return [checked_nums[addition], index]

        checked_nums[number] = index

print(twoSum([2,7,11,15], 9))