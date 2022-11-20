"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:

    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here

        intervals.sort(key=lambda i: i.start)
        for i, interval in enumerate(intervals):
            if i == 0 :
                first_interval = intervals[i]
                continue
            if first_interval.end > interval.start:
                return False
            first_interval = interval
        return True