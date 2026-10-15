class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = defaultdict(int)
        for task in tasks:
            freq[task] += 1
        
        timestamp = 0
        max_heap = []
        for task, count in freq.items():
            heapq.heappush(max_heap, (-count, task))
        
        min_heap = []

        
        while max_heap or min_heap:
            while min_heap and min_heap[0][0] + n + 1  <= timestamp:
                _, [task, count] = heapq.heappop(min_heap)
                heapq.heappush(max_heap, (count, task))
            
            if max_heap:     
                count, task = heapq.heappop(max_heap)
                count += 1
                if count < 0:
                    heapq.heappush(min_heap, (timestamp, [task, count]))

            # print(max_heap, min_heap)
            timestamp += 1

        return timestamp
"""
n = 3

AAABC

freq -> maxHeap
    A - 3
    b - 1
    c - 1

temp
timestamp = 0


cooldown -> minHeap
[0, (A, 1)]
0. 1.  2.  3.   4
A , B, C, idl -> A _. id -> idl -> id -> A
timetamp += 1
"""