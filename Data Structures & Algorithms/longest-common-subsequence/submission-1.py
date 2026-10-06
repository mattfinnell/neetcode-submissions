class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self._lcs(text1, text2, 0, 0, {})

    def _lcs(self, text1, text2, i, j, memo):
        if i == len(text1) or j == len(text2):
            return 0

        if (i, j) in memo:
            return memo[(i, j)]

        if text1[i] == text2[j]:
            memo[(i, j)] = self._lcs(text1, text2, i + 1, j + 1, memo) + 1
            return memo[(i, j)]

        memo[(i, j)] = max(
            self._lcs(text1, text2, i + 1, j, memo),
            self._lcs(text1, text2, i, j + 1, memo),
        )

        return memo[(i, j)] 