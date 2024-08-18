# 74. Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/


from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row_left = 0
        row_right = len(matrix) - 1

        target_row = -1

        while row_left <= row_right:
            row_mid = (row_left + row_right) // 2

            if target < matrix[row_mid][0]:
                row_right = row_mid - 1
            elif target > matrix[row_mid][-1]:
                row_left = row_mid + 1
            else:
                target_row = row_mid

                break

        col_left = 0
        col_right = len(matrix[target_row]) - 1

        while col_left <= col_right:
            col_mid = (col_left + col_right) // 2

            if target == matrix[target_row][col_mid]:
                return True
            elif target < matrix[target_row][col_mid]:
                col_right = col_mid - 1
            else:
                col_left = col_mid + 1

        return False
