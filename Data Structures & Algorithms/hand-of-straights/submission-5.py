class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0: return False

        freq = defaultdict(int)
        for num in hand:        # n
            freq[num] += 1

        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            start = min_heap[0]

            for num in range(start, start + groupSize):   # n
                if freq[num] == 0: return False
                freq[num] -= 1
                if freq[num] == 0:
                    if num != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)                 # logn

        return True


"""
1234 5678 9-10-11-12

1,2,4,2,3,5,3,4

12345

start = min(set)
freq[start] -= 1

for i in range(1, groupSize):
    num = start + i
    if num not in set: return False

    freq[num] -= 1
    if freq[num] == 0:
        set.remove(num)

return True

1 -> 1
2 -> 2
3 -> 3
4 -> 2
5 -> 1

len(hand) % groupSize != 0 -> return False
"""