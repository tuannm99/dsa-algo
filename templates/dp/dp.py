from bisect import bisect_left


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def coin_change(coins: list[int], amount: int) -> int:
    inf = float("inf")
    dp = [0] + [inf] * amount

    for coin in coins:
        for value in range(coin, amount + 1):
            dp[value] = min(dp[value], dp[value - coin] + 1)

    return -1 if dp[amount] == inf else int(dp[amount])


def length_of_lis(nums: list[int]) -> int:
    tails: list[int] = []
    for num in nums:
        idx = bisect_left(tails, num)
        if idx == len(tails):
            tails.append(num)
        else:
            tails[idx] = num
    return len(tails)


def knapsack_01(weights: list[int], values: list[int], capacity: int) -> int:
    dp = [0] * (capacity + 1)
    for i in range(len(weights)):
        for cap in range(capacity, weights[i] - 1, -1):
            dp[cap] = max(dp[cap], dp[cap - weights[i]] + values[i])
    return dp[capacity]
