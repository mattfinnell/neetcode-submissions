import heapq

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result = [intervals[0]]

        for start, end in intervals:
            _, current_end = result[-1]

            if start <= current_end:
                result[-1][1] = max(end, current_end)

            else:
                result.append([start, end])

        return result