class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        stack = []
        for string in strs:
            if not stack:
                stack.append(string)
            else:
                temp = self.prefix(string, stack.pop())
                stack.append(temp)

        return stack[0] if stack else ""

    def prefix(self, string_a, string_b):
        res = ""
        if not string_a or not string_b: return res
        l, r = 0, 0
        while l < len(string_a) and r < len(string_b):
            if string_a[l] != string_b[r]:
                return res
            else:
                res += string_a[l]
            
            l += 1
            r += 1
        
        return res