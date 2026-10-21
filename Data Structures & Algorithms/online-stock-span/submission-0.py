class StockSpanner:

    def __init__(self):
        self.stack = []
        self.time = 1

    def next(self, price: int) -> int:
        while self.stack and price >= self.stack[-1][0]:
            self.stack.pop()
        
        if self.stack:
            res = self.time - self.stack[-1][1]
        else:
            res = self.time - 0

        self.stack.append([price, self.time])
        self.time += 1

        return res


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)

"""
collects daily price quotes and return the span of that stock's price

span = max consecutive days (going backwards), stack price <= price that day

100 80  60  70  60  75  85
1   1   1   2   1   4   6

100 85
1   7

while current_price >= stack[-1]: keep popping


include the current day
"""