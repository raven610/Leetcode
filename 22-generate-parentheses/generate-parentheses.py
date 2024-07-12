class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        ans = []
        def generate(leftBrackets,rightBrackets):
            if leftBrackets == n and rightBrackets == n:
                ans.append("".join(stack))
                return
            if leftBrackets < n:
                stack.append("(")
                generate(leftBrackets+1,rightBrackets)
                stack.pop()
            if rightBrackets < n and leftBrackets > rightBrackets:
                stack.append(")")
                generate(leftBrackets,rightBrackets+1)
                stack.pop()

        generate(0,0)
        return ans