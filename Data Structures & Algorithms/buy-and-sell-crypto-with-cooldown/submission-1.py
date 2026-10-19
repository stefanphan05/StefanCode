class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, bought, sold):
            state = (i, bought, sold)
            if state in memo:
                return memo[state]
            if i >= len(prices):
                return 0
            
            # if sold -> gotta skip this day
            if sold:
                memo[state] = dfs(i + 1, False, False)
                return memo[state]
            
            # if bought
                # sell today

                # wait
            
            # not bought
                # buy today

                # wait
            
            if bought:
                memo[state] = max(dfs(i + 1, False, True) + prices[i], dfs(i + 1, True, False))
            else:
                memo[state] = max(dfs(i + 1, True, False) - prices[i], dfs(i + 1, False, False))
            return memo[state]
        
        return dfs(0, False, False)