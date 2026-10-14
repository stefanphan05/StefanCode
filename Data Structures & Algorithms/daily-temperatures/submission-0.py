class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, tem in enumerate(temperatures):
            while stack and tem > stack[-1][0]:
                _, j = stack.pop()
                res[j] = i - j
            
            stack.append([tem, i])

        return res

"""
0, 1, 2, 3, 4, 5, 6
30,38,30,36,35,40,28
i

1, 4, 1, 2, 1, 0, 0

(40, 5), (26, 6)
n

"""