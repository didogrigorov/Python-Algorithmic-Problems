def isPalindrom(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
        if not s[right].isalnum():
            right -= 1

        if s[left].lower() != s[right].lower():
            return f"false"

        left += 1
        right -= 1

    return f"true"


word = "madame"
print(isPalindrom(word))
