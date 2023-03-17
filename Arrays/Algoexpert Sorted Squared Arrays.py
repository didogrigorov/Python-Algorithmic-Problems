def sortedSquaredArray(array):
    # Write your code here.
    squared_list = []
    for num in array:
        result = num ** 2
        squared_list.append(result)
    return sorted(squared_list)