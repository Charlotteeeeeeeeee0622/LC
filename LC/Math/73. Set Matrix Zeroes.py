class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowzero = set()
        colzero = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    rowzero.add(r)
                    colzero.add(c)

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if r in rowzero or c in colzero:
                    matrix[r][c] = 0

        return matrix