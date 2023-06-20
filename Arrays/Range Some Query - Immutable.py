from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        self.prefix = []
        current = 0
        for n in nums:
            current += n
            self.prefix.append(current)

    def sumRange(self, left: int, right: int) -> int:
        right_sum = self.prefix[right]
        print(right_sum)
        left_sum = self.prefix[left - 1] if left > 0 else 0
        print(left_sum)

        return right_sum - left_sum