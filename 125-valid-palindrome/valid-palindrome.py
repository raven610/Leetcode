class Solution:
    def isAlpha(self,s):
        return ((ord(s) >= ord('a') and ord(s) <= ord('z')) or (ord(s) >= ord('0') and ord(s) <= ord('9')))
    def isPalindrome(self, s: str) -> bool:
        L = 0
        s = s.lower()
        R = len(s)-1
        while L <= R:
            #print(s[L],s[R],L,R)
            if not self.isAlpha(s[L]):
                L+=1
            elif not self.isAlpha(s[R]):
                R-=1
            elif s[L] != s[R]:
                return False
            else:
                L+=1
                R-=1
        return True
