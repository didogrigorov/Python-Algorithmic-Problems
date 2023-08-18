def maxProduct(s: str) -> int:
    N, pali = len(s), {}

    for mask in range(1, 1 << N):
        subseq = ""
        for i in range(N):
            if mask & (1 << i):
                subseq += s[i]

        if subseq == subseq[::-1]:
            pali[mask] = len(subseq)
    res = 0

    for mask1 in pali:
        for mask2 in pali:
            if mask1 & mask2 == 0:
                res = max(res, pali[mask1] * pali[mask2])

    return res

print(maxProduct("leetcodecom"))