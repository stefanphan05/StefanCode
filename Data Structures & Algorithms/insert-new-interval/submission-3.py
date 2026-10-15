class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        i = 0
        res = []

        new_start, new_end = newInterval
        while i < N and intervals[i][1] < new_start:
            res.append(intervals[i])
            i += 1
        
        while i < N and new_end >= intervals[i][0]:
            new_start = min(new_start, intervals[i][0])
            new_end = max(new_end, intervals[i][1])
            i += 1
        
        res.append([new_start, new_end])

        while i < N:
            res.append(intervals[i])
            i += 1

        return res