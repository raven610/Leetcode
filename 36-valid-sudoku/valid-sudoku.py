class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        r = defaultdict(set)
        c = defaultdict(set)
        g = defaultdict(set)
        rc = len(board)
        cc = len(board[0])
        for i in range(rc):
            for j in range(cc):
                if board[i][j] != '.':
                    if (board[i][j] in r[i]) or (board[i][j] in c[j]) or (board[i][j] in g[(i//3,j//3)]):
                        return False
                    r[i].add(board[i][j])
                    c[j].add(board[i][j])
                    g[(i//3,j//3)].add(board[i][j])
        return True