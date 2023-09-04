import collections
from typing import List


def distinctNames(ideas: List[str]) -> int:
  word_map = collections.defaultdict(set)

  for w in ideas:
    word_map[w[0]].add(w[1:])

  res = 0

  for char1 in word_map:
    for char2 in word_map:
      if char1 == char2:
        continue
      intersect = 0
      for w in word_map[char1]:
        if w in word_map[char2]:
          intersect += 1

      distinct1 = len(word_map[char1]) - intersect
      distinct2 = len(word_map[char2]) - intersect
      res += distinct1 * distinct2

  return res