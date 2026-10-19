class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        def dfs(i, total):
            state = (i, total)
            if state in memo:
                return memo[state]
            if total == amount: return 1
            if total > amount or i >= len(coins): return 0
            
            memo[state] = dfs(i, total + coins[i]) + dfs(i + 1, total)
            return memo[state]
        
        return dfs(0, 0)