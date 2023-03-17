def productSum(array, depth = 1):
    if len(array) == 0:
        return 0
    if type(array[0]) == list:
        new_depth = depth + 1
        return (new_depth * productSum(array[0], new_depth)) + productSum(array[1:], depth)
    else:
        return array[0] + productSum(array[1:], depth)