class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {0: 1, 1: 1}
        return self._climbStairs(n, memo)

    def _climbStairs(self, n: int, memo) -> int:
        if n in memo:
            return memo[n]

        result = self._climbStairs(n - 1, memo) + self._climbStairs(n - 2, memo)
        memo[n] = result
        return result