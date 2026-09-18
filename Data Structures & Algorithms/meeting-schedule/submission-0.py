"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x: x.start)

        for a, b in zip(sorted_intervals[:-1], sorted_intervals[1:]):
            if a.end > b.start:
                return False

        return True