def maxVowels(s: str, k: int) -> int:
    vowels = {"a", "e", "u", "i", "o"}

    left, cnt, res = 0, 0, 0

    for r in range(len(s)):
        if s[r] in vowels:
            cnt += 1

        if r - left + 1 > k:
            if s[left] in vowels:
                cnt -= 1
            left += 1

        res = max(res, cnt)

    return res


print(maxVowels("abciiidef", 3))