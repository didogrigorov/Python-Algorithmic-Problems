class Solution:
    def partitionString(self, s: str) -> int:
        current_set = set()
        result = 1

        for c in s:
            if c in current_set:
                result += 1
                current_set = set()
            current_set.add(c)

        return result