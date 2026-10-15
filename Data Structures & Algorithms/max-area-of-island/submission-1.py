class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        R, C = len(grid), len(grid[0])
        res = 0
        directions = [(1, 0), (-1,0), (0, 1), (0, -1)]

        def backtrack(r, c):
            if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] != 1:
                return 0
            
            grid[r][c] = 0
            area = 1
            for dr, dc in directions:
                area += backtrack(r + dr, c + dc)
            
            return area

        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    res = max(backtrack(r, c), res)

        return res