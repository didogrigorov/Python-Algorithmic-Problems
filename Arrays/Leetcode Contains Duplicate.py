def containsDuplicate(nums):
    numbers = set()

    for i in range(len(nums)):

        if nums[i] in numbers:
            return True

        numbers.add(nums[i])

    return False

nums = [1,2,3,4]
print(containsDuplicate(nums))