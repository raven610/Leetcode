class Solution:
    def numberOfSteps(self, num: int) -> int:
        c = 0
        while num != 0:
            num = num//2 if (num%2 == 0) else num - 1
            c += 1
        return c
