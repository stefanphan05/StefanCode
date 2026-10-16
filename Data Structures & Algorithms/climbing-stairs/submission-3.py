class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        memo = {}
        def dfs(i):
            if i >= n:
                return i == n
            if i in memo:
                return memo[i]
            
            ways = dfs(i + 1) + dfs(i + 2)
            memo[i] = ways
            return ways

        return dfs(0)