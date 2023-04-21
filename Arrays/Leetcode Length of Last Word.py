def lengthOfLastWord(s):
    length = 0

    for char in s[::-1]:
        if char == ' ':
            if length >= 1:
                return length
        else:
            length += 1

    return length

print(lengthOfLastWord("Hello World"))