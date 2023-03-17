def binarySearch(array, target):
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2

        if array[mid] < target:
            low = mid + 1
            if low > len(array) - 1:
                return -1
        else:
            high = mid
    return low if array[low] == target else -1

print(binarySearch([1, 5, 23, 111], 111))