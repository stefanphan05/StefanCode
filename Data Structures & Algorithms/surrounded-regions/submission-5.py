class Solution:
    def solve(self, board: List[List[str]]) -> None:
        R, C = len(board), len(board[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        def dfs_border(r, c):
            """
            Turn every O in the border to T
            """
            if r < 0 or c < 0 or r >= R or c >= C or board[r][c] != "O": return

            board[r][c] = "T"
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                dfs_border(nr, nc)

        for c in range(C):
            if board[0][c] == "O":
                dfs_border(0, c)
            if board[R - 1][c] == "O":
                dfs_border(R - 1, c)
        for r in range(R):
            if board[r][0] == "O":
                dfs_border(r, 0)
            if board[r][C - 1] == "O":
                dfs_border(r, C - 1)

        for r in range(R):
            for c in range(C):
                if board[r][c] == "O":
                    board[r][c] = "X"
        
        for r in range(R):
            for c in range(C):
                if board[r][c] == "T":
                    board[r][c] = "O"

"""
Reverse thinking

- Turn every O that are at the border into T
- Turn the rest of O into X
- Turn the T back to O again


XOXX
OXOX
XOXO
OXOX
"""