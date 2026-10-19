class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        res = []
        l, r = 0, 0
        curr_char = set()
        while r < len(s):
            char_r = s[r]
            curr_char.add(char_r)
            freq[char_r] -= 1
            if freq[char_r] == 0:
                is_correct = True
                for char in curr_char:
                    if freq[char] != 0:
                        is_correct = False
                
                if is_correct:
                    res.append(r - l + 1)
                    l = r + 1

            r += 1

        return res