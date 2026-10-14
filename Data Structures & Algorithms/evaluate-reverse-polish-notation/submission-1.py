class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ["+", "-", "*", "/"]

        for token in tokens:
            if token in operators:
                num_one, num_two = int(stack.pop()), int(stack.pop())
                if token == "+":
                    res = num_one + num_two
                elif token == "-":
                    res = num_two - num_one
                elif token == "*":
                    res = num_one * num_two
                else:
                    res = num_two / num_one
                
                stack.append(res)
            else:
                stack.append(token)
        
        return int(stack[-1])