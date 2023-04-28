def isIsomorphic(s: str, t: str) -> bool:
    dictS, dictT = {}, {}

    for i in range(len(s)):
        c1, c2 = s[i], t[i]

        if (c1 in dictS and dictS[c1] != c2) or (c2 in dictT and dictT[c2] != c1):
            return False

        dictS[c1] = c2
        dictT[c2] = c1

    return True