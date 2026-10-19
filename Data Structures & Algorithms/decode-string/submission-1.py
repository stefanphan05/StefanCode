class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char == "]":
                temp = ""
                while stack[-1] != "[":
                    temp = stack.pop() + temp
                
                stack.pop()     # Pop the open bracket
                num = stack.pop()           # get the count
                stack.append(temp * num)
            elif char.isdigit():
                if stack and isinstance(stack[-1], int):
                    stack[-1] = stack[-1] * 10 + int(char)
                else:
                    stack.append(int(char))
            else:
                stack.append(char)
        
        return "".join(stack)

"""
2[a23[b]]c

abbbabbbc

could be 1-1000 (INF)
always a num before [

using stack
    reach ]
    num * temp

always assumpt s is a valid string
"""