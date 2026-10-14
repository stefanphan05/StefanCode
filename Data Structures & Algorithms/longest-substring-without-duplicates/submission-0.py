class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r, res = 0, 0, 0
        curr = defaultdict(int)

        while r < len(s):
            char_r = s[r]  
            if char_r in curr:
                while l < r and char_r in curr:
                    char_l = s[l]
                    curr[char_l] -= 1
                    if curr[char_l] == 0:
                        del curr[char_l]
                    l += 1
            
            curr[char_r] += 1
            res = max(res, r - l + 1)
            r += 1
        
        return res

"""
abcabcbb

"""