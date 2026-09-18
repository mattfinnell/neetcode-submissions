import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)

        frequencies = [(-count, key) for (key, count) in counter.items()]
        frequencies.sort()

        return [key for _, key in frequencies[:k]]