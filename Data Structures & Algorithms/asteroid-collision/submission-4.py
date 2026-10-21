class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if stack and ast < 0 and stack[-1] > 0:         # Negative
                has_equal = False
                while stack and stack[-1] > 0 and abs(ast) >= stack[-1]:
                    if abs(ast) == stack[-1]:
                        has_equal = True
                        stack.pop()
                        break
                    stack.pop()

                if stack and abs(ast) < stack[-1] or has_equal:
                    continue

            stack.append(ast)
        return stack

"""
collide when
    current is negative, prev is positive
        current = prev -> both explode
        abs(current) > prev -> prev explode
        abs(current) < prev -> current explode

7   -3  9   -15     12      3

7 -3

2   4   3   -4  -1

4   4    
"""