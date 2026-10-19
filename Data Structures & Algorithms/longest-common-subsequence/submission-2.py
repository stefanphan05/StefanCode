class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        S1, S2 = len(text1), len(text2)
        memo = {}
        def dfs(l, r):
            state = (l, r)
            if state in memo:
                return memo[state]
            if l >= S1 or r >= S2:
                return 0
            
            if text1[l] == text2[r]:
                memo[state] = 1 + dfs(l + 1, r + 1)
            else:
                memo[state] = max(dfs(l + 1, r), dfs(l, r + 1))

            return memo[state]
        
        return dfs(0, 0)
"""
cat                 crabt
"""