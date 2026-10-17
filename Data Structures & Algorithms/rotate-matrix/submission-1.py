class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        R, C = len(matrix), len(matrix[0])
        t, b = 0, R - 1

        while t < b:
            l, r = t, b
            print(t, b, l, r)
            for i in range(r - l):
                temp = matrix[t][l + i]
 
                print(t, i, temp)
                # Top right
                new_temp = matrix[t + i][r]
                print(new_temp)
                matrix[t + i][r] = temp     # WRONG

                # Bottom right
                temp = matrix[b][r - i]
                matrix[b][r - i] = new_temp

                # Bottom left
                new_temp = matrix[b - i][l]
                matrix[b - i][l] = temp

                # Top left
                matrix[t][l + i] = new_temp

                print(matrix)
            
            t += 1
            b -= 1


"""
5   1   9   11
2   4   8   10
13  3   6   7
15  14  12  16

15  13  2   5
14   4   8   1
12  3   6   9
16  7  10  11


1   2   3
4   5   6
7   8   9

7   2   1
4   5   6
9   8   3

7   4   1
8   5   2
9   6   3

1   2   3   4   5
6   7   8   9   10
11  12  13  14  15
16  17  18  19  20
21  22  23  24  25

t = 0           l = 0
b = 4           r = 4

temp = 1
new_temp = 5


"""