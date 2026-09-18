class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        table, l, max_length = {}, 0, 0

        for r in range(len(s)):
            if s[r] in table:
                l = max(table[s[r]] + 1, l)
            
            table[s[r]] = r
            max_length = max(max_length, r - l + 1)
        
        return max_length
