class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = float("inf")
        prices = [INF] * n
        prices[src] = 0

        for _ in range(k + 1):
            temp = prices.copy()

            for from_i, to_i, price_i in flights:
                if prices[from_i] == INF: continue

                if prices[from_i] + price_i < temp[to_i]:
                    temp[to_i] = prices[from_i] + price_i
            
            prices = temp
        
        return prices[dst] if prices[dst] != INF else -1