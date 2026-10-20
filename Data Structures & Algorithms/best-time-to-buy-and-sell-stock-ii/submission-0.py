class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        memo = {}
        def dfs(i, buy):
            state = (i, buy)
            if state in memo:
                return memo[state]
            if i >= len(prices):
                return 0
            
            # if buy:
            # sell today or nah

            # not buy:
                # buy today
                # nah
            
            if buy:
                memo[state] = max(dfs(i + 1, False) + prices[i], dfs(i + 1, True))
            else:
                memo[state] = max(dfs(i + 1, True) - prices[i], dfs(i + 1, False))

            return memo[state] 

        return dfs(0, False)