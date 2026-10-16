class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        memo = {}
        def dfs(i, rob_prev, rob_first):
            if i >= N: 
                return 0

            oops = (i, rob_prev, rob_first)

            if oops in memo: 
                return memo[oops]

            # Last house
            if i == N - 1 and rob_first:
                return 0

            if not rob_prev:
                profit = dfs(i + 1, False, rob_first)
                if i == 0:
                    profit = max(dfs(i + 1, True, True) + nums[i], profit)
                else:
                    profit = max(dfs(i + 1, True, rob_first) + nums[i], profit)
            else:
                profit = dfs(i + 1, False, rob_first)
            
            memo[oops] = profit
            return profit
        
        return dfs(0, False, False)