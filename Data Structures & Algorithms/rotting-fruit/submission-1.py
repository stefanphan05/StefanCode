class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = deque()
        num_of_fresh_fruit = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 2:
                    queue.append((r, c, 0))
                if grid[r][c] == 1:
                    num_of_fresh_fruit += 1
        
        res = 0
        while queue:
            r, c, time = queue.popleft()
            res = max(res, time)

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
                    num_of_fresh_fruit -= 1
                    grid[nr][nc] = 2
                    queue.append((nr, nc, time + 1))

        if num_of_fresh_fruit == 0:
            return res
        return -1

"""
2   1   1
0   1   1
1   0   1
"""