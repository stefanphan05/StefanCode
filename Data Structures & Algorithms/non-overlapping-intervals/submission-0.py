class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        intervals.sort()

        stack = []
        for i in range(N):
            if i == 0:
                stack.append(intervals[i])
                continue

            start, end = intervals[i]
            prev_start, prev_end = stack[-1]
            
            if start < prev_end:
                if end < prev_end:
                    stack[-1] = start, end
            else:
                stack.append([start, end])

        return N - len(stack)