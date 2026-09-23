from collections import Counter
from pprint import pprint

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter, frequencies = (
            Counter(nums), 
            [[] for _ in range(len(nums) + 1)]
        )

        for num, frequency in counter.items():
            frequencies[frequency].append(num)

        result = []
        for items in reversed(frequencies):
            for item in items:
                result.append(item)

                if len(result) == k:
                    return result