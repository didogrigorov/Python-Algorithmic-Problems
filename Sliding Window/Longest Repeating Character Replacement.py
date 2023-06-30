def characterReplacement(s: str, k: int) -> int:
    counter = {}
    result = 0
    left = 0

    for right in range(len(s)):
        counter[s[right]] = 1 + counter.get(s[right], 0)

        while (right - left + 1) - max(counter.values()) >= k:
            counter[s[left]] -= 1
            left += 1

        result = max(result, right - left + 1)

    return result


s = "AABABBA"
k = 2
print(characterReplacement(s, k))
