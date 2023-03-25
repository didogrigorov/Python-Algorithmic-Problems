def findNumbers(nums):
    counter = 0

    for item in nums:

        if len(str(item)) % 2 == 0:
            counter +=1

    return counter


nums = [12,345,2,6,7896]

print(findNumbers(nums))