from collections import defaultdict

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest, num_set = 0, set(nums)

        for n in num_set:
            if (n - 1) not in num_set:
                length = 1

                while (n + length) in num_set:
                    length += 1

                longest = max(length, longest)

        return longest
