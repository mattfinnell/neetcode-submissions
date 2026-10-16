from collections import Counter

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        counter, result = Counter(nums), []
        min_value, max_value = min(nums), max(nums)

        for num in range(min_value, max_value + 1):
            result.extend([num] * counter[num])

        return result