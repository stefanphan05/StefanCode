class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        R, C = len(heights), len(heights[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def can_flow_to_pacific(r, c):
            return r == 0 or c == 0

        def can_flow_to_atlantic(r, c):
            return r == R - 1 or c == C - 1

        def dfs_pacific(r, c, prev, visit):
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visit: return False

            if heights[r][c] > prev:
                return False

            if can_flow_to_pacific(r, c):
                return True
            
            visit.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs_pacific(nr, nc, heights[r][c], visit):
                    return True
            
            return False 

        def dfs_atlantic(r, c, prev, visit):
            if r < 0 or r >= R or c < 0 or c >= C or (r, c) in visit: return False

            if heights[r][c] > prev:
                return False

            if can_flow_to_atlantic(r, c):
                 return True
            
            visit.add((r, c))
    
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if dfs_atlantic(nr, nc, heights[r][c], visit):
                    return True
            
            return False     
        
        res = []
        for r in range(R):
            for c in range(C):
                if dfs_pacific(r, c, heights[r][c], set()) and dfs_atlantic(r, c, heights[r][c], set()):
                    res.append([r, c])
    
        return res