class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.subMatrix = []
        for i in range(len(matrix)):
            total = 0
            sublist = []
            for j in range(len(matrix[0])):
                total += matrix[i][j]
                sublist.append(total)
            print(sublist)
            self.subMatrix.append(sublist)
                

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        s = 0
        for i in range(row1,row2+1):
            s += self.subMatrix[i][col2] - self.subMatrix[i][col1-1] if col1 > 0 else self.subMatrix[i][col2]
        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)