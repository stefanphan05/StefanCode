class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []

        for num in range(n + 1):
            count = bin(num).count('1')
            res.append(count)
        
        return res