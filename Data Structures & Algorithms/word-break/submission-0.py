class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        return self._word_break(s, set(wordDict), 0, {})

    def _word_break(self, s: str, words: List[str], i, memo) -> bool:
        if i == len(s):
            return True

        if i in memo:
            return memo[i]

        for j in range(i, len(s)):
            if s[i : j + 1] in words:
                if self._word_break(s, words, j + 1, memo):
                    memo[i] = True
                    return True

        memo[i] = False
        return False