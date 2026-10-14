class Solution:
    def isValid(self, s: str) -> bool:
        parens = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for paren in s:
            if paren in parens.keys():
                if not stack or stack[-1] != parens[paren]:
                    return False
                stack.pop()
            else:
                stack.append(paren)
        
        return len(stack) == 0