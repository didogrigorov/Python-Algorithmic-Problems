def arrayOfProducts(array):
    products = [1] * len(array)

    left_product = 1
    for i in range(len(array)):
        products[i] = left_product
        left_product *= array[i]

    right_product = 1
    for j in reversed(range(len(array))):
        products[j] *= right_product
        right_product *= array[j]

    return products


array = [5, 1, 4, 2]
print(arrayOfProducts(array))