def fizzBuzz(n):
    solution = [0] * n

    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            solution[i - 1] = "FizzBuzz"
        elif i % 3 == 0:
            solution[i - 1] = "Fizz"
        elif i % 5 == 0:
            solution[i - 1] = "Buzz"
        else:
            solution[i - 1] = str(i)

    return solution


print(fizzBuzz(15))