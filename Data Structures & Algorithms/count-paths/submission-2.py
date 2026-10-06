class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        return self._unique_paths(m, n, 0, 0, {})


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
