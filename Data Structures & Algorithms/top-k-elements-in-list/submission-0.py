class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for num in nums:    # n
            freq[num] += 1
        
        min_heap = []
        for num, count in freq.items():
            if len(min_heap) < k:
                heapq.heappush(min_heap, [count, num])
                continue
            
            if count > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, [count, num])
        
        res = []
        for _, num in min_heap:
            res.append(num)

        return res
"""
[1,2,2,3,3,3, 4, 5, 5,5,5], k = 3
n

min_heap
len(heap) = k
(1, 4), (4, 5)

1 -> 1
2 -> 2
3 -> 3
4 -> 1
5 -> 4

[1, 1], [2, 2], 

nlogn


"""