#approach 2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c1 = [0]*26
        c2 = [0]*26
        for i in s:
            c1[ord(i)-ord('a')] += 1
        for i in t:
            c2[ord(i)-ord('a')] += 1
        for i in range(26):
            if c1[i] != c2[i]:
                return False
        return True
