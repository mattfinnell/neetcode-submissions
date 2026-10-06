class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1

        low, high = min(m, n), max(m, n)
        result = j = 1
        for i in range(low, high + low - 1):
            result *= i
            result //= j
            j += 1

        return result


    def _unique_paths(self, m: int, n: int, i, j, memo): # dfs
        if (i, j) == (m - 1, n - 1):
            return 1

        if i >= m or j >= n:
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        result = (
            self._unique_paths(m, n, i, j + 1, memo) + 
            self._unique_paths(m, n, i + 1, j, memo)
        )

        memo[(i, j)] = result

        return result
