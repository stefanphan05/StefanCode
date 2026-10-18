class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq = defaultdict(int)

        for num in hand:        # n
            freq[num] += 1

        hand_set = set(hand)
        while hand_set:             # n
            start = min(hand_set)
            freq[start] -= 1
            if freq[start] == 0:
                hand_set.remove(start)

            for i in range(1, groupSize):   # n
                num = start + i
                if num not in hand_set: return False
                freq[num] -= 1
                if freq[num] == 0:
                    hand_set.remove(num)

        return True


"""
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