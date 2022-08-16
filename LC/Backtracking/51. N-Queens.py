# https://leetcode.com/problems/n-queens/discuss/19971/Python-recursive-dfs-solution-with-comments.
from typing import List

if __name__ == '__main__':

    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtracking(index):
            if index == len(queens):
                res.append(queens)
                return  # backtracking
            for i in range(len(queens)):
                queens[index] = i
                if valid(index):
                    backtracking(index + 1)

        def valid(n):
            for i in range(n):
                if abs(queens[i] - queens[n]) == n - i:
                    return False
                if queens[i] == queens[n]:
                    return False
            return True

        def make_board(queens):
            n = len(queens)
            board = []
            board_temp = [['.'] * n for _ in range(n)]
            for row, col in enumerate(queens):
                board_temp[row][col] == 'Q'
            for row in board_temp:
                board.append(''.join(row))
            return board

        def make_all_boards(res):
            actual_boards = []
            for queens in res:
                actual_boards.append(make_board(queens))
            return actual_boards

        n = 4
        queens = [-1] * n
        res = []
        backtracking(0)
        return make_all_boards(res)




