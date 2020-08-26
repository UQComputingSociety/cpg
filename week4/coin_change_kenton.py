from functools import lru_cache


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        x = solve(tuple(coins), amount)
        if x == float("inf"):
            return -1
        return x


@lru_cache(maxsize=None)
# returns minimum number of coins needed to make 'amount'
# solve(1) .. solve(1)
def solve(coins, amount):
    if amount == 0:
        return 0
    m = float("inf")
    for c in coins:
        if amount < c:
            continue
        x = 1 + solve(coins, amount - c)
        if x < m:
            m = x
    return m
