from collections import Counter
from pprint import pprint


def maxNumberOfBalloons(text: str) -> int:

    count_text = Counter(text)
    pprint(count_text)

    balloon = Counter("balloon")
    pprint(balloon)

    result = len(text)

    for char in balloon:
        result = min(result, count_text[char] // balloon[char])

    return result

text = "nlaebolko"
print(maxNumberOfBalloons(text))