class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        coins.sort()
        return self._change(amount, coins, 0, {})

    def _change(self, amount, coins, i, memo):
        if (i, amount) in memo:
            return memo[(i, amount)]

        if amount == 0:
            return 1

        if i >= len(coins):
            return 0

        result = 0
        if amount >= coins[i]:
            result = self._change(amount, coins, i + 1, memo)
            result += self._change(amount - coins[i], coins, i, memo)

        memo[(i, amount)] = result
        return result
