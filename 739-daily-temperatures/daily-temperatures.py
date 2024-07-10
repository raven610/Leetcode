class Stack:
    def __init__(self):
        self.stack = []
    def push(self,element):
        self.stack.append(element)
    def pop(self):
        try:
            element = self.stack.pop()
        except:
            element = -1
        return element
    def top(self):
        if len(self.stack) > 0:
            return self.stack[-1]
        return -1

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0]*n
        stack = Stack()
        for i in range(n):
            #print(stack.stack,ans)
            if i > 0:
                days = 1
                while (stack.top() != -1) and (temperatures[i] > stack.top()[1]):
                    element = stack.pop()
                    ans[element[0]] = i - element[0]
                    days += 1
            stack.push([i,temperatures[i]])
        #while stack.top() != -1:
        #    ans[i] = 0
        #    stack.pop()
        return ans