class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        N = len(digits)
        res = []
        def backtrack(i, curr):
            if i >= N:
                if len(curr) == N and curr != "":
                    res.append(curr)
                return

            for char in digit_map[digits[i]]:
                backtrack(i + 1, curr + char)
            
        backtrack(0, "")
        return res