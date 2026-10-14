class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        seen = defaultdict(int)
        for char in s:
            seen[char] += 1
        
        for char in t:
            if char not in seen:
                return False
            seen[char] -= 1
            if seen[char] == 0:
                del seen[char]

        return True
    
"""
gotta be same length
len(s) != len(t) -> retrun False

char -> freq
r -> 2
a -> 2
c -> 2
e -> 1
"""