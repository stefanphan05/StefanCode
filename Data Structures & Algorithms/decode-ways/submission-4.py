class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        self.count = 0
        memo = {}
        def dfs(i):
            if i >= N:
                return 1
            if s[i] == "0":
                return 0
            if i in memo:
                return memo[i]
            
            ways = 0
            if (s[i] == "1" or s[i] == "2") and i + 1 < N:
                if s[i] == "2":
                    if s[i + 1] in ["0", "1", "2", "3", "4", "5", "6"]:
                        ways += dfs(i + 2)
                else:
                    ways += dfs(i + 2)

            ways += dfs(i + 1)
            memo[i] = ways
            return ways
        return dfs(0)


"""
digit start is 1 or 2, there are multiple ways after that
"""