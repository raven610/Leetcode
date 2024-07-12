class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        posToSpeed = [(position[i],speed[i]) for i in range(n)]
        posToSpeed.sort(key=lambda x: x[0], reverse=True)
        stack = []
        for i in posToSpeed:
            if len(stack) > 0:
                if (target-i[0])/i[1] > stack[-1]:
                    stack.append((target-i[0])/i[1])
            else:
                stack.append((target-i[0])/i[1])
        return len(stack)