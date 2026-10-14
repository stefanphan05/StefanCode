class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_freq = [0] * 26
        for char in s1:
            index = ord(char) - ord('a')
            s1_freq[index] += 1
        
        l, r = 0, 0
        curr_freq = [0] * 26
        while r < len(s2):
            char_r = s2[r]
            index = ord(char_r) - ord('a')
            curr_freq[index] += 1
            if r - l + 1 < len(s1):
                r += 1
                continue
            
            if s1_freq == curr_freq: return True
            char_l = s2[l]
            index = ord(char_l) - ord('a')
            curr_freq[index] -= 1
            l += 1
            r += 1

        return False
            