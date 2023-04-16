# def caesarCipherEncryptor(string, key):
#     new_string = []
#     newkey = key % 26
#
#     for letter in string:
#         new_string.append(getNewLetter(letter, newkey))
#
#     return ''.join(new_string)
#
# def getNewLetter(letter, key):
#
#     newLetterCode = ord(letter) + key
#
#     if newLetterCode <= 122:
#         return chr(newLetterCode)
#     else:
#         return chr(96 + newLetterCode % 122)
def caesarCipherEncryptor(string, key):
    result = []

    for letter in string:
        oldValue = ord(letter) - 97
        newValue = (oldValue + key) % 26
        newLetter = chr(97 + newValue)
        result.append(newLetter)

    return "".join(result)

print(caesarCipherEncryptor("xyz", 210))