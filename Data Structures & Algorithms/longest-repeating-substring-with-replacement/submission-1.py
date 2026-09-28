from collections import Counter 

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count, result = Counter(), 0

        i, j, maxf = 0, 0, 0
        while j < len(s):
            count[s[j]] += 1
            maxf = max(maxf, count[s[j]])

            while (j - i + 1) - maxf > k:
                count[s[i]] -= 1
                i += 1

            result = max(result, j - i + 1)
            
            j += 1

        return result