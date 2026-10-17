class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def dfs(i, has_started, has_stopped):
            state = (i, has_started, has_stopped)
            if state in memo:
                return memo[state]
            if has_stopped:
                return 0
            if i >= N:
                if not has_started:
                    return float("-inf")
                return 0
            
            # has_start
                # Keep going
                # Stop here
            if has_started:
                largest = max(dfs(i + 1, True, False) + nums[i], dfs(i, True, True))
            # has not started
                # start here
                # wait
            else:
                largest = max(dfs(i + 1, True, False) + nums[i], dfs(i + 1, False, False))
                print("Hey")
            
            memo[state] = largest
            return largest

        
        return dfs(0, False, False)