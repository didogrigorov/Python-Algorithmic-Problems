coins = [1, 1, 1 ,1, 1]


def nonConstructibleChange(coins):
    # Write your code here.
    coins.sort()
    coins_sum = 0

    for coin in coins:
        if coin > coins_sum + 1:
            return coins_sum + 1

        coins_sum += coin

    return coins_sum + 1

print(nonConstructibleChange(coins))