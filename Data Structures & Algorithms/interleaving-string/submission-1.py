class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        S1, S2, S3 = len(s1), len(s2), len(s3)
        if S1 + S2 != S3: return False

        memo = {}
        def dfs(i, l, r):
            state = (i, l, r)
            if state in memo:
                return memo[state]
            if i >= S3:
                return True
            
            if l < S1 or r < S2: 
                if l < S1 and r < S2:
                    if s3[i] == s1[l]:
                        if dfs(i + 1, l + 1, r):
                            memo[state] = True
                            return True
                    if s3[i] == s2[r]:
                        if dfs(i + 1, l, r + 1):
                            memo[state] = True
                            return True
                    if s3[i] != s1[l] and s3[i] != s2[r]:
                        memo[state] = False
                        return False
                elif l < S1:
                    if s3[i] != s1[l]: 
                        memo[state] = False
                        return False
                    if dfs(i + 1, l + 1, r): 
                        memo[state] = True
                        return True
                else:
                    if s3[i] != s2[r]:
                        memo[state] = False
                        return False
                    if dfs(i + 1, l, r + 1):
                        memo[state] = True
                        return True
            
            memo[state] = False
            return False
        
        return dfs(0, 0, 0)

"""
abc         xyz


abxzcy
"""