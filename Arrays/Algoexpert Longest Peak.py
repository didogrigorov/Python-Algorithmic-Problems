def longestPeak(array):
    longestPeakLength = 0
    i = 1

    while i < len(array) - 1:
        havePeak = array[i - 1] < array[i] and array[i] > array[i + 1]

        if not havePeak:
            i += 1
            continue

        left_index = i - 2
        while left_index >= 0 and array[left_index] < array[left_index + 1]:
            left_index -= 1

        right_index = i + 2
        while right_index < len(array) and array[right_index] < array[right_index - 1]:
            right_index += 1

        currentLongestPeak = right_index - left_index - 1
        longestPeakLength = max(longestPeakLength, currentLongestPeak)
        i = right_index

    return longestPeakLength

array = [1, 2, 3, 3, 4, 0, 10, 6, 5, -1, -3, 2, 3]

print(longestPeak(array))