def twoNumberSum(array, targetSum):
    numbers= []
    for i in range(len(array)):
        for j in range(i + 1, len(array)):
            if j == i:
                continue
            result = array[i] + array[j]
            if result == targetSum:
                numbers.append(array[i])
                numbers.append(array[j])
    return numbers