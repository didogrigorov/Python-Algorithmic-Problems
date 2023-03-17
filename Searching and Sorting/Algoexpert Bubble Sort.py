def bubblesort(array):
    for i in range(0, len(array) - 1):
        for j in range(0, len(array) - 1 - i):
            if array[j] > array[j + 1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

array = list(map(int, input().split(",")))
print(', '.join(str(x) for x in bubblesort(array)))