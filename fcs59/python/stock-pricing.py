
def max_profit(prices):

    profits = []
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            profits.append(prices[i] - prices[i-1])

    return max(profits)

print(max_profit([5, 7, 2]))