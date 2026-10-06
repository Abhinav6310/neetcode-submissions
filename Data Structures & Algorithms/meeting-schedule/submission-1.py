"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        max_ = 0
        intervals.sort(key=lambda i: i.start)
        for i in intervals:
            if i.start<max_:
                return False
            if i.end>max_:
                max_ = i.end
        return True