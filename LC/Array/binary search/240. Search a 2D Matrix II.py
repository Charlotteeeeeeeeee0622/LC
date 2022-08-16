# https://leetcode.com/problems/search-a-2d-matrix-ii/discuss/528263/Two-efficient-python-sol.-sharing.-90%2B-w-Diagram
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        h = len(matrix)
        w = len(matrix[0])

        for row in matrix:
            if row[0] <= target <= row[-1]:

                left = 0
                right = w - 1

                while left <= right:
                    mid = left + (right - left) // 2
                    mid_value = row[mid]

                    if mid_value < target:
                        left = mid + 1
                    elif mid_value > target:
                        right = mid - 1
                    else:
                        return True

        return False

