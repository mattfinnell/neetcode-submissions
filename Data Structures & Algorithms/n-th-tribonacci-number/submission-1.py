class Solution:
    def tribonacci(self, n: int) -> int:
        return self._tribonacci(n, {0: 0, 1: 1, 2: 1})

    def _tribonacci(self, n: int, memo: Dict[int, int]) -> int:
        if n in memo:
            return memo[n]

        memo[n] = sum((self._tribonacci(i, memo) for i in range(n - 3, n)))

        return memo[n]