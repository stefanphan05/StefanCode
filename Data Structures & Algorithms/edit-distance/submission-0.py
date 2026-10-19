class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        M, N = len(word1), len(word2)
        memo = {}
        def dfs(l, r):
            state = (l, r)
            if state in memo:
                return memo[state]
            if l == M:
                return N - r
            if r == N:
                return M - l
            
            if word1[l] == word2[r]:
                memo[state] = dfs(l + 1, r + 1)
            else:
                # Do one of the 3 operations
                res = min(dfs(l + 1, r), dfs(l, r + 1))
                res = min(dfs(l + 1, r + 1), res)
                memo[state] = res + 1
            
            return memo[state]
        
        return dfs(0, 0)