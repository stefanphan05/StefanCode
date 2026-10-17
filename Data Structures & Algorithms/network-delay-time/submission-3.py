class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = defaultdict(list)
        for u, v, t in times:
            adj[u].append((v, t))

        min_heap = [(0, k)]
        visit = set()
        res = 0
        while min_heap:
            curr_time, curr_node = heapq.heappop(min_heap)

            if curr_node in visit: continue
            visit.add(curr_node) 

            res = curr_time

            for nei, weight in adj[curr_node]:
                if nei not in visit:
                    heapq.heappush(min_heap, (curr_time + weight, nei))
        
        if len(visit) != n: return -1
        return res