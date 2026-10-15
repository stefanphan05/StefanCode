"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda x: x.start)
        stack = []
        for interval in intervals:
            start, end = interval.start, interval.end
            if stack and start < stack[-1][1]:
                return False
            
            stack.append([start, end])
        
        return True