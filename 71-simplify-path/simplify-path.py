class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        return self.stack.pop()
    def top(self):
        try:
            tp = self.stack[-1]
            return tp
        except:
            return None

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = Stack()
        n = len(path)
        i = 1
        while i < n:
            s = ""
            while i<n and path[i] != '/':
                s += path[i]
                i += 1
            while i<n and path[i] == '/':
                i += 1
            print(s)
            if s != '':
                if s == '..':
                    if stack.top() != None:
                        stack.pop()
                elif s == '.':
                    continue
                else:
                    stack.push(s)
        ans = ""
        while stack.top() != None:
            ans = '/' + stack.pop() + ans
        if ans == "":
            return '/'
        return ans