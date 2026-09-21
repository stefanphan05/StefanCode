class Solution:
    def commonFactors(self, a: int, b: int) -> int:
        la = set()
        count = 0
        if b > a:
            a, b = b, a

        for i in range(1, a + 1):
            if a % i == 0:
                la.add(i)
        
        for i in range(1, b + 1):
            if b % i == 0:
                if i in la:
                    count += 1

        return count