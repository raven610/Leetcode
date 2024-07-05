class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        L = 0
        R = 0
        n = len(s)
        n2 = len(t)
        while L < n and R < n2:
            if s[L] == t[R]:
                L += 1
            R += 1
        if L == n:
            return True
        return False