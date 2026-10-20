class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        R, C = len(matrix), len(matrix[0])
        self.matrix = matrix
        self.sum_matrix = [[0] * C for _ in range(R)]
        for r in range(R):
            prefix_sum = 0
            for c in range(C):
                prefix_sum += matrix[r][c]
                if r == 0:
                    self.sum_matrix[r][c] = prefix_sum
                else:
                    self.sum_matrix[r][c] = prefix_sum + self.sum_matrix[r - 1][c]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        top, left, bottom, right = row1, col1, row2, col2
        sum_till_bottom_right = self.sum_matrix[bottom][right]
        if top == 0 and left == 0:
            return sum_till_bottom_right
        elif top == 0:
            sum_left = self.sum_matrix[bottom][left - 1]
            return sum_till_bottom_right - sum_left
        elif left == 0:
            sum_top = self.sum_matrix[top - 1][right]
            return sum_till_bottom_right - sum_top
        else:
            sum_left = self.sum_matrix[bottom][left - 1]
            sum_top = self.sum_matrix[top - 1][right]
            sum_top_left = self.sum_matrix[top - 1][left - 1]
            return sum_till_bottom_right - sum_left - sum_top + sum_top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)