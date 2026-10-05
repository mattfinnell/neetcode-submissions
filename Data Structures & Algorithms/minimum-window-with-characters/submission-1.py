from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        required, remaining = Counter(t), len(t)
        left, right, result = 0, 0, ""

        for right, char in enumerate(s):
            # update required and remaining across the right pointer
            if char in required:
                if required[char] > 0:
                    remaining -= 1
                required[char] -= 1

            # window contains all required characters
            while not remaining: 
                # Update result
                if not result or right - left  + 1 < len(result):
                    result = s[left:right + 1]

                # repair required table and update remaining
                left_char = s[left]
                if left_char in required:
                    required[left_char] += 1
                    if required[left_char] > 0:
                        remaining += 1

                # increment left
                left += 1

        return result