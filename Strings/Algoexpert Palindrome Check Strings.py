def isPalindrome(string):
    # Write your code here.
    new_string = [*string]
    palindrom_checker = ''
    for i in range(len(new_string)):
        char = new_string.pop()
        palindrom_checker += char

    if palindrom_checker == string:
        return True
    else:
        return False