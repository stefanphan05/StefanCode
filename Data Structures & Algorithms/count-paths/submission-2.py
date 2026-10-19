class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        R, C = m, n
        
        memo = {}
        def dfs(r, c):
            state = (r, c)
            if state in memo:
                return memo[state]
            if r < 0 or c < 0 or r >= R or c >= C:
                return 0
            if r == R - 1 and c == C - 1:
                return 1
            
            res = 0
            res += dfs(r + 1, c)
            res += dfs(r, c + 1)

            memo[state] = res
            return res
        
        return dfs(0, 0)