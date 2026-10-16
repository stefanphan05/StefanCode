class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = {}

        def dfs(i, left, right):
            state = (i, left, right)
            if state in memo:
                return memo[state]
            if i >= N:
                if left == right:
                    return True
                return False

            num = nums[i]

            # Put in the left
            if dfs(i + 1, left + num, right):
                memo[state] = True
                return True

            # Put in the right
            if dfs(i + 1, left, right + num): 
                memo[state] = True
                return True

            memo[state] = False
            return False
        
        return dfs(0, 0, 0)