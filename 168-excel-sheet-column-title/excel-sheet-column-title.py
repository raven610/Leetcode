import math
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        s = ''
        while columnNumber > 0:
            c = chr((columnNumber-1)%26 + 65)
            s = c + s
            columnNumber = (columnNumber -1) //26
        return s