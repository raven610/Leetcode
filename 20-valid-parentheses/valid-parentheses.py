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
    def isValid(self, s: str) -> bool:
        stack = Stack()
        for i in s:
            if i == '{' or i == '(' or i == '[':
                stack.push(i)
            else:
                if len(stack.stack) == 0:
                    return False
                if (i == '}' and stack.top() == '{') or (i == ']' and stack.top() == '[') or (i == ')' and stack.top() == '('):
                    stack.pop()
                else:
                    return False
        if len(stack.stack) == 0:
            return True
        return False