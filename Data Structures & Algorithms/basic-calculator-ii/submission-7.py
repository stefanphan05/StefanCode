class Solution:
    def calculate(self, s: str) -> int:
        cleaned_s = []
        i = 0
        while i < len(s):               # Clean the empty spaces and convert all nums to int
            char = s[i]                  
            if char.isdigit():
                temp = int(char)
                j = i + 1
                while j < len(s) and s[j].isdigit():
                    temp = temp * 10 + int(s[j])
                    j += 1
                cleaned_s.append(temp)
                i = j
            elif char in ["+", "-", "*", "/"]:
                cleaned_s.append(char)
                i += 1
            else:
                i += 1

        stack = []
        i = 0
        while i < len(cleaned_s):
            char = cleaned_s[i]
            if char in ["*", "/"]:
                prev_num, next_num = stack.pop(), cleaned_s[i + 1]
                if char == "*":
                    temp = prev_num * next_num
                else:
                    temp = int(prev_num / next_num)
                stack.append(temp)
                i += 2
            else:
                stack.append(char)
                i += 1
        
        another_stack = []
        i = 0
        while i < len(stack):
            char = stack[i]
            if char in ["+", "-"]:
                prev_num, next_num = another_stack.pop(), stack[i + 1]
                if char == "+":
                    temp = prev_num + next_num
                else:
                    temp = prev_num - next_num
                another_stack.append(temp)
                i += 2
            else:
                another_stack.append(char)
                i += 1

        return another_stack[0]