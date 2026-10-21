class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        N = len(intervals)
        stack = []
        i = 0
        new_start, new_end = newInterval

        # Add intervals come BEFORE new_interval (end < new_start)
        while i < N and intervals[i][1] < new_start:
            stack.append(intervals[i])
            i += 1

        # Add the overlap
        while i < N and (intervals[i][0] <= new_start <= intervals[i][1] or new_start <= intervals[i][0] <= new_end):
            new_start = min(intervals[i][0], new_start)
            new_end = max(intervals[i][1], new_end)
            i += 1
        stack.append([new_start, new_end])

        # Add intervals come AFTER new_interval
        while i < N:
            stack.append(intervals[i])
            i += 1
        
        return stack