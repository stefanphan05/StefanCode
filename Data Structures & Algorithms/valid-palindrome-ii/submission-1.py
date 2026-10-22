class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left = s[l + 1: r + 1]  # Skip the one on the l
                right = s[l : r]        # Skip the one on the r
                return left == left[::-1] or right == right[::-1]
            l += 1
            r -= 1
        
        return True