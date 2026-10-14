class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_stack:
            self.min_stack.append(val)
        else:
            curr_sm_value = self.min_stack[-1]
            if val < curr_sm_value:
                self.min_stack.append(val)
            else:
                self.min_stack.append(curr_sm_value)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]


1, 2, 0
1, 1, 0