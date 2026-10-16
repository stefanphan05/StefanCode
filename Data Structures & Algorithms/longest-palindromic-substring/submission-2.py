class Solution:
    def longestPalindrome(self, s: str) -> str:
        S = len(s)
        res = ""
        if S == 1: return s

        for i in range(1, S):
            if s[i - 1] == s[i]:    # Even case
                l, r = i - 1, i
                while l >= 0 and r < S and s[l] == s[r]:
                    if (r - l + 1) > len(res):
                        res = s[l:r+1]
                    r += 1
                    l -= 1
                    
            # Odd case
            l, r = i, i
            while l >= 0 and r < S and s[l] == s[r]:
                if (r - l + 1) > len(res):
                    res = s[l:r+1]
                r += 1
                l -= 1      

        return res