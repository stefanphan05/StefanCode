class Solution:
    def canJump(self, nums: List[int]) -> bool:
        memo = {}
        def dfs(i):
            if i in memo:
                return memo[i]

            if i >= len(nums) - 1:
                memo[i] = True
                return True
            
            if nums[i] == 0:
                memo[i] = False
                return False
            
            for num in range(1, nums[i] + 1):
                if dfs(i + num):
                    return True
            
            memo[i] = False
            return False
        
        return dfs(0)