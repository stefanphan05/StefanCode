class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        t, b = 0, len(matrix) - 1
        correct_row = -1

        while t <= b:
            row = (t + b) // 2
            if target < matrix[row][0]:
                b = row - 1
            elif target > matrix[row][-1]:
                t = row + 1
            else:
                correct_row = row
                break

        if correct_row == -1:
            return False
        
        l, r = 0, len(matrix[0]) - 1
        while l <= r:
            m = (l + r) // 2
            if matrix[correct_row][m] == target:
                return True
            elif target > matrix[correct_row][m]:
                l = m + 1
            else:
                r = m - 1

        return False

"""
row = 0
1
1
1 <= 0

"""