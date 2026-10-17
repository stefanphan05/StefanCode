class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res = []
        t, b = 0, len(matrix) - 1
        l, r = 0, len(matrix[0]) - 1

        while l <= r and t <= b:
            for i in range(l, r + 1):
                res.append(matrix[t][i])
            t += 1

            for i in range(t, b + 1):
                res.append(matrix[i][r])
            r -= 1

            if l > r or t > b: break

            for i in range(r, l - 1, -1):
                res.append(matrix[b][i])
            b -= 1
            print(res)

            if l > r or t > b: break

            for i in range(b, t - 1, -1):
                res.append(matrix[i][l])
            l += 1


        return res

"""
1   2   3
4   5   6
7   8   9

2   5   8
4   0   -1

t=1
b=1
l=0
r=1

258-1
"""