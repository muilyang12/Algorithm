# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_row = len(grid)
        num_col = len(grid[0])

        def dfs(grid, row, column):
            if row < 0 or row >= num_row:
                return
            if column < 0 or column >= num_col:
                return

            if grid[row][column] == "1":
                grid[row][column] = "3"
            elif grid[row][column] == "0":
                return
            elif grid[row][column] == "3":
                return

            dfs(grid, row - 1, column)
            dfs(grid, row + 1, column)
            dfs(grid, row, column - 1)
            dfs(grid, row, column + 1)

        result = 0

        for i in range(num_row):
            for j in range(num_col):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    result += 1

        return result
