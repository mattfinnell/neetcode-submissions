import heapq

class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        heap, i, result = [], 0, {}

        for query in sorted(queries):
            while i < len(intervals) and intervals[i][0] <= query:
                a, b = intervals[i]
                heapq.heappush(heap, (b - a + 1, b))
                i += 1

            while heap and heap[0][1] < query:
                heapq.heappop(heap)
            
            result[query] = heap[0][0] if heap else - 1

        return [result[query] for query in queries]