class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        def backtrack(curr, start, end):
            if len(curr) == n * 2:
                if start == n and end == n:
                    res.append("".join(curr))
                return
            
            curr.append("(")
            print(curr)
            backtrack(curr[:], start + 1, end)
            curr.pop()
            if start > end:
                curr.append(")")
                backtrack(curr[:], start, end + 1)


        backtrack([], 0, 0)
        return res