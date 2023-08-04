from typing import List


def longestConsecutive(nums: List[int]) -> int:
    nums_set = set(nums)
    longest_sequence = 0

    for num in nums:
        if (num - 1) not in nums_set:
            length = 0
            while (num + length) in nums_set:
                length += 1
            longest_sequence = max(length, longest_sequence)
    return longest_sequence

print(longestConsecutive([100,4,200,1,3,2]))