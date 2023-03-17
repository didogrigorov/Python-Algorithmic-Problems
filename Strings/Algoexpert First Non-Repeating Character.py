def firstNonRepeatingCharacter(string):
    # Write your code here.
    dict_counter = {}
    for char in string:
        if char not in dict_counter:
            dict_counter[char] = 0
        dict_counter[char] += 1

    for key,value in dict_counter.items():
      if dict_counter[key] == 1:
          result = string.index(key)
          return result
          break
    else:
        return - 1