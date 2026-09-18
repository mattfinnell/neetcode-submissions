class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(xi**2 + xj**2, (xi, xj)) for xi, xj in points]
        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for _ in range(k)]