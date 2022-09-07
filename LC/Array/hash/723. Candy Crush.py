class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board or not board[0]: return board
        board = self.transpose_clockwise(board)
        m, n = len(board), len(board[0])
        while True:
            crushed_candy = set()
            for i in range(m):
                for j in range(2, n):
                    if board[i][j] and board[i][j] == board[i][j - 1] and board[i][j] == board[i][j - 2]:
                        crushed_candy |= {(i, j), (i, j - 1), (i, j - 2)}
            for j in range(n):
                for i in range(2, m):
                    if board[i][j] and board[i][j] == board[i - 1][j] and board[i][j] == board[i - 2][j]:
                        crushed_candy |= {(i, j), (i - 1, j), (i - 2, j)}
            if not crushed_candy: break
            for x, y in crushed_candy:
                board[x][y] = 0

            for i in range(m):
                row = [v for v in board[i] if v != 0]
                board[i] = row + [0] * (n - len(row))
        for _ in range(3):
            board = self.transpose_clockwise(board)
        return board

    def transpose_clockwise(self, board):
        m, n = len(board), len(board[0])
        output = [[0] * m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                output[j][m - 1 - i] = board[i][j]
        return output