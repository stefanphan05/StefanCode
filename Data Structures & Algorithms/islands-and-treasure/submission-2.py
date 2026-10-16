class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        R, C = len(grid), len(grid[0])
        INF = 2147483647
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def is_inbound(r, c):
            return 0 <= r < R and 0 <= c < C

        def is_unvisited_land(r, c):
            return grid[r][c] == INF

        def bfs(queue):
            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if is_inbound(nr, nc) and is_unvisited_land(nr, nc):
                        grid[nr][nc] = 1 + grid[r][c]
                        queue.append((nr, nc))

        # Start from every treasure backwards
        queue = deque()
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 0:
                    queue.append((r, c))

        bfs(queue)
"""
INF     -1      0       INF
INF     INF     INF     -1
INF     -1      INF     -1
0       -1      INF     INF

val

"""