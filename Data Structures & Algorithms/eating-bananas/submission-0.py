class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        res = max(piles)
        l, r = 1, max(piles)
        while l <= r:
            m = (l + r) // 2
            total_hrs = 0
            for pile in piles:
                remain, divider = pile % m, pile // m
                total_hrs += divider
                if remain > 0:
                    total_hrs += 1

            print(m, total_hrs)
            if total_hrs <= h:
                res = min(res, m)
                r = m - 1
            else:
                l = m + 1

        return res

"""
1 -> max(piles)

logm x n
"""