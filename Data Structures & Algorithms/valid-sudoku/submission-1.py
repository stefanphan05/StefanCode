class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rols = defaultdict(set)
        cols = defaultdict(set)
        boxes = defaultdict(set)

        for r in range(9):
            for c in range(9):
                curr = board[r][c]
                if curr == ".": continue

                r_sm, c_sm = r // 3, c // 3
                box = (r_sm, c_sm)

                if curr in rols[r] or curr in cols[c] or curr in boxes[box]:
                    return False
                
                rols[r].add(curr)
                cols[c].add(curr)
                boxes[box].add(curr)

        return True