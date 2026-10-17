class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n not in seen:
            seen.add(n)
            total = 0
            
            while n > 0:
                total += (n % 10) ** 2
                n = n // 10
            
            n = total
            if n == 1:
                return True

        return False