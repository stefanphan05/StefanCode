class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        pac, atl = set(), set()
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c, visit, prev):
            if r < 0 or r >= R or c < 0 or c >= C or heights[r][c] < prev or (r, c) in visit:
                return
            
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, visit, heights[r][c])
        
        # COL ~ 0 or C - 1
        for r in range(R):
            dfs(r, 0, pac, 0)
            dfs(r, C - 1, atl, 0)
        
        # ROW ~ 0 or R - 1
        for c in range(C):
            dfs(0, c, pac, 0)
            dfs(R - 1, c, atl, 0)
        
        res = []
        for r in range(R):
            for c in range(C):
                if (r, c) in pac and (r, c) in atl:
                    res.append((r, c))
        
        return res