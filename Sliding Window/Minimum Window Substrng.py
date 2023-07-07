def minWindow(s: str, t: str) -> str:
    if t == "": return ""

    countT, window = {}, {}

    for char in t:
        countT[char] = 1 + countT.get(char, 0)

    have, need = 0, len(countT)
    res, resLen = [-1, -1], float("infinity")
    left = 0

    for r in range(len(s)):
        c = s[r]
        window[c] = 1 + window.get(c, 0)

        if c in countT and window[c] == countT[c]:
            have += 1
            while have == need:
                if (r - left + 1) < resLen:
                    res = [left, r]
                    resLen = (r - left + 1)

                window[s[left]] -= 1

                if s[left] in countT and window[s[left]] < countT[s[left]]:
                    have -= 1

                left += 1

    l, r = res
    return s[l:r + 1] if resLen != float("infinity") else ""


s = "ADOBECODEBANC"
t = "ABC"
print(minWindow(s, t))