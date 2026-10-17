class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        
        zero_rows = set()
        zero_cols = set()

        for r in range(R):
            for c in range(C):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)
        
        for r in zero_rows:
            for i in range(C):
                matrix[r][i] = 0
        
        for c in zero_cols:
            for i in range(R):
                matrix[i][c] = 0
        
       
"""
0   1   2   0
3   4   5   2
1   3   1   5
"""