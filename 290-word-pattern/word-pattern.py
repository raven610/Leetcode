class Solution:
    def wordPattern(self, s: str, t: str) -> bool:
        d = {}
        n = len(s)
        t = t.split(' ')
        if len(t) != n:
            return False
        for i in range(n):
            if ((s[i] in d) and (t[i] != d[s[i]])) or (t[i] in d.values() and (s[i] not in d)):
                return False
            else:
                d[s[i]] = t[i]
        return True
