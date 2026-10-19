class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        res = []
        max_heap = []
        temp = None
        if a != 0:
            heapq.heappush(max_heap, [-a, "a"])
        
        if b != 0:
            heapq.heappush(max_heap, [-b, "b"])
        
        if c != 0:
            heapq.heappush(max_heap, [-c, "c"])

        while max_heap:
            count, char = heapq.heappop(max_heap)
            res.append(char)
            count += 1

            if temp:
                temp_count, temp_char = temp
                temp = None
                heapq.heappush(max_heap, [temp_count, temp_char])

            if count == 0: continue
            if len(res) > 1 and res[-1] == char and res[-2] == char:
                temp = [count, char]
            else:
                heapq.heappush(max_heap, [count, char])

        return "".join(res)

"""
babaabbcc

a = 2
b = 2
c = 2

return "" if couldnt

a = 0
b = 1
c = 5

cc

max_heap to hold the maximum occurence
temp array
"""