class Solution:
    def validPalindrome(self, s: str) -> bool:
        def is_palindrome(le, ri):
            while le < ri:
                if s[le] != s[ri]: return False
                le += 1
                ri -= 1
            
            return True


        l, r = 0, len(s) - 1
        while l < r:
            if s[l] != s[r]:
                left = s[l + 1: r + 1]  # Skip the one on the l
                right = s[l : r]        # Skip the one on the r
                return is_palindrome(l + 1, r) or is_palindrome(l, r - 1)
            l += 1
            r -= 1
        
        return True