from typing import List
def maxProfit(prices: List[int]) -> int:
    left = 0 # buying
    right = 1 # selling
    max_profit = 0

    while right < len(prices):
        if prices[left] < prices[right]:
            profit = prices[right] - prices[left]
            max_profit = max(max_profit, profit)
        else:
            left = right

        right += 1

    return max_profit

prices = [7,6,4,3,1]
print(maxProfit(prices))