class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j, deleted = 0, len(s) - 1, False

        while i < j:
            if s[i] != s[j]:
                return (
                    self._is_palindrome(s, i + 1, j) or
                    self._is_palindrome(s, i, j - 1)
                )

            i += 1
            j -= 1

        return True

    def _is_palindrome(self, s, i, j):
        while i < j:
            if s[i] != s[j]:
                return False

            i += 1
            j -= 1

        return True
