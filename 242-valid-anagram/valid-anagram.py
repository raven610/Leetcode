class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for i in t:
            if i in d:
                d[i] -= 1
                if d[i] == 0:
                    del d[i]
            else:
                return False
        if len(d.keys()) == 0:
            return True
        return False