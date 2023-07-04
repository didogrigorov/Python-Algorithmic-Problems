def minFlips(s: str) -> int:
    n = len(s)
    s = s + s
    alt1, alt2 = "", ""

    for i in range(len(s)):
        alt1 += "0" if i % 2 else "1"
        alt2 += "1" if i % 2 else "0"

    res = len(s)
    diff1, diff2 = 0, 0
    left = 0

    for r in range(len(s)):
        if s[r] != alt1[r]:
            diff1 += 1
        if s[r] != alt2[r]:
            diff2 += 1

        if (r - left + 1) > n:
            if s[left] != alt1[left]:
                diff1 -= 1
            if s[left] != alt2[left]:
                diff2 -= 1
            left += 1

        if (r - left + 1) == n:
            res = min(res, diff1, diff2)

    return res


print(minFlips("111000"))