class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def top(self):
        return self.stack[-1]

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = Stack()
        for i in tokens:
            if i in ['+','-','*','/']:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    c = a+b
                elif i == '-':
                    c = a-b
                elif i == '*':
                    c = a*b
                elif i == '/':
                    c = int(a/b)
                stack.push(c)
            else:
                stack.push(int(i))
        return stack.top()