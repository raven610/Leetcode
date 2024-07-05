class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        self.stack.pop()
    def peep(self):
        return self.stack[-1]
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = Stack()
        for i in operations:
            if i == 'D':
                x = int(stack.peep())*2
                stack.push(x)
            elif i == '+':
                prev = int(stack.peep())
                stack.pop()
                prev2 = int(stack.peep())
                stack.push(int(prev))
                stack.push(prev+prev2)
            elif i == 'C':
                stack.pop()
            else:
                stack.push(int(i))
        s = 0
        return sum(stack.stack)