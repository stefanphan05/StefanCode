class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        for stone in stones:
            heapq.heappush(max_heap, -stone)
        
        while len(max_heap) > 1:
            x, y = heapq.heappop(max_heap), heapq.heappop(max_heap)
            if x != y:
                heapq.heappush(max_heap, -abs(x - y))
        
        if max_heap != []:
            return -max_heap[0]
        return 0