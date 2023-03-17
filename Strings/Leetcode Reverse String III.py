word_input = input()
chars_list = [*word_input]

temporary_list = []
mirrored_words = ''

for char in range(len(chars_list)):
    if chars_list[char] == " ":
        reversed_words = temporary_list[::-1]
        mirrored_words += ''.join(reversed_words)
        mirrored_words += " "
        temporary_list = []
    else:
        temporary_list.append(chars_list[char])

if len(temporary_list) > 0:
    reversed_words = temporary_list[::-1]
    mirrored_words += ''.join(reversed_words)
print(mirrored_words)