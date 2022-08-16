# https://leetcode.com/problems/word-search/discuss/27660/Python-dfs-solution-with-comments.
from typing import List


class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def dfs(self, board, i, j, word):
        if len(word)==0:
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False
        temp=board[i][j]
        board[i][j]='#'
        res=self.dfs(board,i-1,j,word[1:]) or self.dfs(board,i,j-1,word[1:])\
        or self.dfs(board,i+1,j,word[1:]) or self.dfs(board,i,j+1,word[1:])
        board[i][j]=temp
        return res


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtracking(board, r, c, word):
            if len(word) == 0:
                return True
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]) or word[0] != board[r][c]:
                return False
            temp = board[r][c]
            board[r][c] = '#'
            res = backtracking(board, r, c + 1, word[1:]) or backtracking(board, r + 1, c, word[1:]) or \
                  backtracking(board, r - 1, c, word[1:]) or backtracking(board, r, c - 1, word[1:])
            board[r][c] = temp
            return res

        if not board:
            return False
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtracking(board, r, c, word):
                    return True
        return False
