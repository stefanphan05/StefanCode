class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        def dfs(i, total):
            state = (i, total)
            if state in memo:
                return memo[state]
            if i >= len(nums):
                if total == target:
                    return 1
                return 0
            
            # Plus
            memo[state] = dfs(i + 1, total + nums[i]) + dfs(i + 1, total - nums[i])
            return memo[state]
        
        return dfs(0, 0)