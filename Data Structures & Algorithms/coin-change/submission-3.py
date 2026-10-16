class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        N = len(coins)
        memo = {}
        INF = float("inf")

        def dfs(curr_sum):
            if curr_sum >= amount:
                if curr_sum == amount:
                    return 0
                return INF
            state = (curr_sum)
            if state in memo:
                return memo[state]

            best = INF
            for coin in coins:
                best = min(dfs(curr_sum + coin) + 1, best)

            memo[state] = best
            return best
        
        res = dfs(0) 
        return -1 if res == INF else res