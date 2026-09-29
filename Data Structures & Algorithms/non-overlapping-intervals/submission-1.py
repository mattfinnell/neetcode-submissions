class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        previous, result = intervals[0][1], 0
        for current_start, current_end in intervals[1:]:
            if current_start < previous:
                previous = min(current_end, previous)
                result += 1

            else:
                previous = current_end

        return result