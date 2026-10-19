class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        freq = defaultdict(int)
        for char in s:
            freq[char] += 1
        
        res = []
        l, r = 0, 0
        curr_freq = defaultdict(int)
        while r < len(s):
            char_r = s[r]
            curr_freq[char_r] += 1
            if curr_freq[char_r] == freq[char_r]:
                is_correct = True
                for curr_char, curr_values in curr_freq.items():
                    if curr_values != freq[curr_char]:
                        is_correct = False
                
                if is_correct:
                    res.append(r - l + 1)
                    l = r + 1

            r += 1

        return res