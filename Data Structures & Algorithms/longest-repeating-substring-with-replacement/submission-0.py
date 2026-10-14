class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l, r = 0, 0
        count = defaultdict(int)
        res = 0

        while r < len(s):
            char_r = s[r]
            count[char_r] += 1

            while (r - l + 1) - (max(count.values())) > k:
                char_l = s[l]
                count[char_l] -= 1
                if count[char_l] == 0:
                    del count[char_l]
                l += 1
                
            res = max(res, r - l + 1)
            r += 1

        return res

"""
ABCAABACA, k = 2

A -> 3
B -> 1
C -> 2

length - the highest count char <= k -> acceptable
"""