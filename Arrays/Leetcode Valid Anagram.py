def isAnagram(s: str, t: str) -> bool:
    word1_symbols, word2_symbols = {}, {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] not in word1_symbols:
            word1_symbols[s[i]] = 0
        word1_symbols[s[i]] += 1

        if t[i] not in word2_symbols:
            word2_symbols[t[i]] = 0
        word2_symbols[t[i]] += 1

    if word1_symbols == word2_symbols:
        return True
    else:
        return False


s = "aacc"
t = "ccaa"
print(isAnagram(s, t))