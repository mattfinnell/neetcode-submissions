class Solution:
    def numDecodings(self, s: str) -> int:
        return self._num_decodings(s, 0, {})

    def _num_decodings(self, s: str, i, memo) -> int:
        if i == len(s):
            return 1

        if i in memo:
            return memo[i]
        
        if s[i] == '0':
            return 0

        result = self._num_decodings(s, i + 1, memo)

        if i < len(s) - 1:
            if (
                s[i] == '1' or 
                (s[i] == '2' and s[i + 1] < '7')
            ):
                result += self._num_decodings(s, i + 2, memo)

        memo[i] = result
        return result

        


