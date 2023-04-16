from collections import defaultdict


def group_anagrams(strs):
    result = defaultdict(list)

    for item in strs:
        count = [0] * 26

        for char in item:
            count[ord(char) - ord("a")] += 1

        result[tuple(count)].append(item)

    return result.values()
