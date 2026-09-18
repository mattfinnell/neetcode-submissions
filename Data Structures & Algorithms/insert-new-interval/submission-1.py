class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []

        for i in range(len(intervals)):
            # NO-CONFLICT: new interval ends before the start of the current interval
            if newInterval[1] < intervals[i][0]:
                result.append(newInterval)
                return result + intervals[i:]

            # NO-CONFLICT: new interval starts beyond the end of the current interval
            elif newInterval[0] > intervals[i][1]:
                result.append(intervals[i])

            # CONFLICT: update the new interval times 
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]

        result.append(newInterval)
        return result