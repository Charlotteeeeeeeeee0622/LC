class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (len(matrix) == 0): return []

        # [6,9]
        # [5,8]
        # [4,7]
        new_matrix = []
        for j in range(len(matrix[0]) - 1, -1, -1):
            new_lst = []
            for i in range(1, len(matrix), 1):
                new_lst.append(matrix[i][j])
            new_matrix.append(new_lst)

        return matrix[0] + self.spiralOrder(new_matrix)
