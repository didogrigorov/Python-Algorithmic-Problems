from typing import List


def fullJustify(words: List[str], maxWidth: int) -> List[str]:
    result = []
    line, length = [], 0
    i = 0

    while i < len(words):
        if length + len(line) + len(words[i]) > maxWidth:

            extra_space = maxWidth - length
            spaces = extra_space // max(1, len(line) - 1)
            remainder = extra_space % max(1, len(line) - 1)

            for j in range(max(1, len(line) - 1)):
                line[j] += " " * spaces
                if remainder:
                    line[j] += " "
                    remainder -= 1

            result.append("".join(line))
            line, length = [], 0

        line.append(words[i])
        length += len(words[i])
        i += 1

    last_line = " ".join(line)
    trail_space = maxWidth - len(last_line)
    result.append(last_line + " " * trail_space)

    return result

words = ["This", "is", "an", "example", "of", "text", "justification."]
print(fullJustify(words, 16))