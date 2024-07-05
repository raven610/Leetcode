class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []

    def push(self, val: int) -> None:
        if self.minstack == [] or self.minstack[-1] >= val:
            self.minstack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        x = self.stack.pop()
        if self.minstack[-1] == x:
            self.minstack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        if self.minstack is []:
            return None
        return self.minstack[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()