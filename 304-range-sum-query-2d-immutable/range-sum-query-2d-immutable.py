# Approach 2
class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.subMatrix = [[0 for i in range(len(matrix[0]))] for i in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i > 0:
                    self.subMatrix[i][j] += self.subMatrix[i-1][j]
                if j > 0:
                    self.subMatrix[i][j] += self.subMatrix[i][j-1]
                if i>0 and j>0:
                    self.subMatrix[i][j] -= self.subMatrix[i-1][j-1]
                self.subMatrix[i][j] += matrix[i][j]
        print(self.subMatrix)  

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        s += self.subMatrix[row2][col2]
        if col1>0 and row1>0:
            s += self.subMatrix[row1-1][col1-1]
        if col1 > 0:
            s -= self.subMatrix[row2][col1-1]
        if row1 > 0:
            s -= self.subMatrix[row1-1][col2]
        return s