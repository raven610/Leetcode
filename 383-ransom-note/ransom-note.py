class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c = [0]*26
        for i in magazine:
            print(ord('a'))
            c[ord(i)-97] += 1
        for i in ransomNote:
            c[ord(i)-97] -= 1
            if c[ord(i)-97] < 0:
                return False
        return True