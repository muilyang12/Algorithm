# 130. Surrounded Regions
# https://leetcode.com/problems/surrounded-regions/


from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        num_row = len(board)
        num_col = len(board[0])

        if num_row < 3 or num_col < 3:
            return

        def dfs(board, row, column):
            if row < 0 or row >= num_row:
                return
            if column < 0 or column >= num_col:
                return

            if board[row][column] == "X" or board[row][column] == "M":
                return

            board[row][column] = "M"

            dfs(board, row - 1, column)
            dfs(board, row + 1, column)
            dfs(board, row, column - 1)
            dfs(board, row, column + 1)

        for i in range(num_row):
            if board[i][0] == "O":
                dfs(board, i, 0)
            if board[i][-1] == "O":
                dfs(board, i, num_col - 1)

        for j in range(num_col):
            if board[0][j] == "O":
                dfs(board, 0, j)
            if board[-1][j] == "O":
                dfs(board, num_row - 1, j)

        for i in range(num_row):
            for j in range(num_col):
                if board[i][j] == "M":
                    board[i][j] = "O"
                elif board[i][j] == "O":
                    board[i][j] = "X"
