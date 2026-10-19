class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        S1, S2, S3 = len(s1), len(s2), len(s3)
        if S1 + S2 != S3: return False

        memo = {}
        def dfs(l, r):
            state = (l, r)
            if state in memo:
                return memo[state]

            if l == S1 and r == S2:
                return True

            i = l + r
            res = (
                l < S1 and s1[l] == s3[i] and dfs(l + 1, r)
            ) or (
                r < S2 and s2[r] == s3[i] and dfs(l, r + 1)
            )
            
            memo[state] = res
            return res
        
        return dfs(0, 0)

"""
abc         xyz


abxzcy
"""