class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            a, b = -heapq.heappop(heap), -heapq.heappop(heap)

            if a == b:
                continue
            
            if a > b:
                heapq.heappush(heap, -(a - b))
        
        return 0 if not heap else -heap[0]