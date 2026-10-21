class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append([v, t])
        
        min_heap = []
        visit = set()
        heapq.heappush(min_heap, (0, k))
        res = 0

        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)
            if curr_node in visit: continue
            res = curr_time
            visit.add(curr_node)

            # print(visit)
            for nei, nei_time in adj[curr_node]:
                if nei not in visit:
                    heapq.heappush(min_heap, [curr_time + nei_time, nei])
        
        return res if len(visit) == n else -1

"""
1 - {1} - 2 - {1} - 3

"""