class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        I = len(cost)
        memo = {}
        def dfs(i):
            if i >= I:
                return 0
            if i in memo:
                return memo[i]
            
            min_cost = min(dfs(i + 1), dfs(i + 2)) + cost[i]
            memo[i] = min_cost
            return min_cost

        return min(dfs(0), dfs(1))

"""
After paying the cost,
can step 1 or 2

can start at 0 or 1
"""