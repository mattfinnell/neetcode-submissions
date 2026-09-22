from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter, heap = Counter(nums), []

        for num in counter.keys():
            heapq.heappush(heap, (counter[num], num))

            if len(heap) > k:
                heapq.heappop(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]