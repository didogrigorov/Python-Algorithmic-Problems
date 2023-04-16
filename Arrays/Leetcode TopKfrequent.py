from typing import List


def topKFrequent(nums: List[int], k: int) -> List[int]:
    counter = {}
    frequency = [[] for i in range(len(nums) + 1)]

    for number in nums:
        counter[number] = 1 + counter.get(number, 0)

    for num, count in counter.items():
        frequency[count].append(num)

    result = []

    for i in range(len(frequency) - 1, 0, -1):
        for n in frequency[i]:
            result.append(n)
            if len(result) == k:
                return result

nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))