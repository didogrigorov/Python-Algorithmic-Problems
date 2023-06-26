class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                skip_left, skip_right = s[left + 1:right + 1], s[left:right]
                return skip_left == skip_left[::-1] or skip_right == skip_right[::-1]

            left += 1
            right -= 1

        return True