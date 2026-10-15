from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(x, y):
            return sqrt(x ** 2 + y ** 2)
        
        max_heap = []
        for x, y in points:
            distance = dist(x, y)
            heapq.heappush(max_heap, [-distance, [x, y]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        
        res = []
        for _, [x, y] in max_heap:
            res.append([x, y]) 
        return res