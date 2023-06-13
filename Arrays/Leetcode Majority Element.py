from typing import List
def majorityElement(nums: List[int]) -> int:
    result = 0
    count = 0

    for n in nums:
        if count == 0:
            result = n
        count += (1 if n == result else -1)

    return result

arr = [1,3,2,1,1,3]
print(majorityElement(arr))