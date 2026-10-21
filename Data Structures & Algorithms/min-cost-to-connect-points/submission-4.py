class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        adj = defaultdict(list)
        for i in range(N):
            xi, yi = points[i]
            for j in range(i + 1, N):
                xj, yj = points[j]
                dist = abs(xi - xj) + abs(yi - yj)
                adj[i].append((j, dist))
                adj[j].append((i, dist))

        res = 0
        visit = set()
        min_heap = [[0, 0]]
        
        while len(visit) < N:
            curr_cost, curr_node = heapq.heappop(min_heap)
            if curr_node in visit: continue

            res += curr_cost
            visit.add(curr_node)
            for nei, cost in adj[curr_node]:
                if nei not in visit:
                    heapq.heappush(min_heap, [cost, nei])
        
        return res