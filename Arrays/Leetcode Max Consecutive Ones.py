
def findMaxConsecutiveOnes(nums):
    counter = 0
    maxcount = 0

    for item in nums:
        if item == 1:
            counter += 1
        else:
            maxcount = max(maxcount, counter)
            counter = 0

    return max(maxcount, counter)



nums = [1,0,1,1,0,1]
print(findMaxConsecutiveOnes(nums))