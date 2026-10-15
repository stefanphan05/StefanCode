class Solution:
    def partition(self, s: str) -> List[List[str]]:
        S = len(s)
        res = []

        def isPali(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1

            return True

        def backtrack(i, curr):
            if i >= len(s):
                res.append(curr[:])
                return

            for j in range(i, S):
                if isPali(s, i, j):
                    curr.append(s[i : j + 1])
                    backtrack(j + 1, curr)
                    curr.pop()

        backtrack(0, [])
        return res
