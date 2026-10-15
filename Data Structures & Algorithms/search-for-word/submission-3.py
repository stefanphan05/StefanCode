class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        R, C = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word): return True
            if r >= R or c >= C or r < 0 or c < 0 or board[r][c] != word[i]: return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                backtrack(r + 1, c, i + 1) or
                backtrack(r - 1, c, i + 1) or
                backtrack(r, c + 1, i + 1) or
                backtrack(r, c - 1, i + 1)
            )

            board[r][c] = temp
            return found

        for r in range(R):
            for c in range(C):
                if board[r][c] == word[0] and backtrack(r, c, 0):
                    return True
        
        return False