class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(math.sqrt(xi**2 + xj**2), (xi, xj)) for xi, xj in points]
        heapq.heapify(heap)

        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        
        return result