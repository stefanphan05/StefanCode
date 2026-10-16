class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 1:
            return 1

        res = 1
        for i in range(1, N):
            # Even
            if s[i - 1] == s[i]:
                l, r = i - 1, i
                while l >= 0 and r < N and s[l] == s[r]:
                    res += 1
                    l -= 1
                    r += 1
            # Odd
            l, r = i, i
            while l >= 0 and r < N and s[l] == s[r]:
                res += 1
                l -= 1
                r += 1

        return res