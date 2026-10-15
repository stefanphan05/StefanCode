class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        R, C = len(grid), len(grid[0])

        def backtrack(r, c):
            if r >= R or c >= C or r < 0 or c < 0 or grid[r][c] != "1":
                return
            
            grid[r][c]= "#"
            backtrack(r + 1, c)
            backtrack(r - 1, c)
            backtrack(r, c + 1)
            backtrack(r, c - 1)

        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    count += 1
                    backtrack(r, c)
        
        return count