"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        N = len(intervals)
        start, end = [], []
        for interval in intervals:
            start.append(interval.start)
            end.append(interval.end)
        
        start.sort()
        end.sort()

        res = 0
        l, r = 0, 0
        count = 0
        while l < N:
            if start[l] < end[r]:
                count += 1
                res = max(res, count)
                l += 1
            else:
                count -= 1
                r += 1

        return res

"""
0-------------------40
  5----10 15----20


"""