class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return 0
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i >= N - 1:
                return 0
            if nums[i] == 0:
                return float("inf")
            
            jumps = float("inf")
            for num in range(1, nums[i] + 1):
                jumps = min(1 + dfs(i + num), jumps)
            
            memo[i] = jumps
            return memo[i]

        return dfs(0)