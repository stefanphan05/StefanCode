class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        i = 0
        while i < len(s):
            char = s[i]
            if char.isdigit():
                temp = int(char)
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    temp = temp * 10 + int(s[j])
                    j += 1
                
                stack.append(temp)
                i = j
                continue

            if char in ["-", "+"] or char == " ":
                if char != " ": 
                    stack.append(char)
                i += 1
                continue
            
            # / and *
            j = i + 1
            next_num = s[j]

            # Skip empty space
            while not next_num.isdigit() and j < len(s):
                j += 1
                next_num = s[j]

            k = j + 1
            while k < len(s) and s[k].isdigit():
                next_num = int(next_num) * 10 + int(s[k])
                k += 1

            prev_num = stack.pop()
            if char == "*":
                temp = int(prev_num) * int(next_num)
            else:
                temp = int(int(prev_num) / int(next_num))
            stack.append(temp)
            i = k
        
        another_stack = []
        i = 0
        while i < len(stack):
            char = stack[i]
            if char in ["-", "+"]:
                prev_num, next_num = another_stack.pop(), stack[i + 1]
                if char == "-":
                    temp = prev_num - next_num
                else:
                    temp = int(prev_num) + int(next_num)
                
                another_stack.append(temp)
                i += 2
            else:
                another_stack.append(char)
                i += 1

        return another_stack[0]

"""
3 + 5 / 2 + 4 + 2

/, *
"""