class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        for char in s: freq[char] += 1
        res = []
        l, r = 0, 0
        open_chars = set()
        while r < len(s):
            char = s[r]
            open_chars.add(char)
            freq[char] -= 1
            if freq[char] == 0:
                open_chars.remove(char)
            if not open_chars:
                res.append(r - l + 1)
                l = r + 1

            r += 1
    

        return res