class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) < 2: # short circuit
            return s

        result, max_length = "", 0
        for i, char in enumerate(s):
            j, left, right = 0, i, i
            while 0 <= left and right < len(s): # odd case
                if s[left] == s[right]:
                    if right - left  + 1 > max_length:
                        result = s[left:right + 1]
                        max_length = right - left + 1

                    j += 1
                    left, right = i - j, i + j
                else:
                    break

            j, left, right = 0, i, i + 1
            while 0 <= left and right < len(s): # even case
                if s[left] == s[right]:
                    if right - left  + 1 > max_length:
                        result = s[left:right + 1]
                        max_length = right - left + 1

                    j += 1
                    left, right = i - j, i + j + 1

                else:
                    break

        return result