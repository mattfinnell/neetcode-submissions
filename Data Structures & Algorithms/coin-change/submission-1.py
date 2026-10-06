from collections import deque

MAX = 1e9

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        min_coins = self._coin_change(coins, amount, {})

        return -1 if min_coins >= MAX else min_coins

    def _coin_change(self, coins, amount, memo) -> int:
        if amount == 0:
            return 0

        if amount in memo:
            return memo[amount]

        result = MAX
        for coin in coins:
            if amount - coin >= 0:
                result = min(
                    result, 
                    self._coin_change(coins, amount - coin, memo) + 1
                )

        memo[amount] = result
        return result