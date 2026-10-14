class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        n = len(prices)
        profit = 0
        while l < n - 1:
            r = l + 1
            while r < n:
                if prices[r] < prices[l]:
                    l = r
                else:
                    profit = max(profit, prices[r] - prices[l])
                    r += 1
            l += 1

        return profit