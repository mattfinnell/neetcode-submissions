from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter, max_frequent, result = Counter(nums), 0, None

        for key, value in counter.items():
            if value > max_frequent:
                result = key
                max_frequent = value

        return result