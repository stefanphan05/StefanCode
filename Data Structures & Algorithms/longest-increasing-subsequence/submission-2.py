class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        INF = float("inf")
        memo = {}
        def dfs(i, has_started, has_stopped, last_num):
            state = (i, has_started, has_stopped, last_num)
            if state in memo: return memo[state]

            if i >= N or has_stopped:
                return 0
            
            num = nums[i]
            longest = 0
            if has_started:
                # Keep going 
                if num > last_num:          # if possible, this num is greater than last_num
                    longest = 1 + dfs(i + 1, True, False, num)
                longest = max(dfs(i + 1, True, False, last_num), longest)    # Skip this num

                # Stopped
                longest = max(dfs(i, True, True, last_num), longest)
            else:
                # Start here
                a = 1 + dfs(i + 1, True, False, num)

                # Wait
                b = dfs(i + 1, False, False, last_num)
                longest = max(a, b)
            
            memo[state] = longest
            return longest
        
        return dfs(0, False, False, min(nums) - 1)