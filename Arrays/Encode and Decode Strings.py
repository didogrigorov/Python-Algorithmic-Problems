from typing import List


def encode(strs: List[str]) -> str:
    """Encodes a list of strings to a single string.
    """
    res = ""
    for s in strs:
        res += str(len(s)) + "#" + s
    return res
# 5#Hello5#World
def decode(str: str) -> List[str]:
    """Decodes a single string to a list of strings.
    """
    res, i = [], 0
    while i < len(str):
        j = i
        while str[j] != "#":
            j += 1
        length = int(str[i:j])
        res.append(str[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res

print(decode("5#Hello5#World"))