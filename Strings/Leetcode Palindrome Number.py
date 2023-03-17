class Solution:
    def isPalindrome(self, n: int) -> bool:
        x = n
        y = 0

        palindrom_logic = lambda: (y * 10) + x % 10

        while x > 0:
            x, y = x//10 , palindrom_logic()

        return y == n