class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        print(intervals)
        res = 0
        stack = []
        for start, end in intervals:
            if not stack:
                stack.append([start, end])
                continue
            
            prev_start, prev_end = stack[-1]
            if start < prev_end:
                if end < prev_end:
                    stack.pop()
                    stack.append([start, end])
                    res += 1
                else:
                    res += 1
            else:
                stack.append([start, end])
        
        return res