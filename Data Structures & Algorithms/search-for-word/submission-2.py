class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROW, COL = len(board), len(board[0])

        def backtrack(r, c, i):
            if i == len(word):
                return True
            if r >= ROW or c >= COL or i == len(word) or r < 0 or c < 0 or board[r][c] != word[i]:
                return False

            temp = board[r][c]
            board[r][c] = "#"       # Mark as already checked
            found = (backtrack(r + 1, c, i + 1) or 
                    backtrack(r - 1, c, i + 1) or 
                    backtrack(r, c + 1, i + 1) or 
                    backtrack(r, c - 1, i + 1))
            
            board[r][c] = temp
            return found
        
        for r in range(ROW):
            for c in range(COL):
                if board[r][c] == word[0]:
                    if backtrack(r, c, 0):
                        return True
        
        return False
"""
ABCE
SFCS
ADEE
"""