class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}

        def dfs(i, rob_prev):
            if i >= N:
                return 0
            if (i, rob_prev) in memo:
                return memo[(i, rob_prev)]
            
            if not rob_prev:
                profit = max(dfs(i + 1, False), dfs(i + 1, True) + nums[i])
            else:
                profit = dfs(i + 1, False)
            
            memo[(i, rob_prev)] = profit
            return profit
        
        return dfs(0, False)