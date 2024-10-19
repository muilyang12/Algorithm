# 289. Game of Life
# https://leetcode.com/problems/game-of-life/

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 0 and self.countLive(board, i, j) == 3:
                    board[i][j] = 2
                elif board[i][j] == 1 and (
                    self.countLive(board, i, j) < 2 or self.countLive(board, i, j) > 3
                ):
                    board[i][j] = 3

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 2:
                    board[i][j] = 1
                elif board[i][j] == 3:
                    board[i][j] = 0

    def countLive(self, board: List[List[int]], row: int, col: int) -> int:
        result = 0

        moves = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        for move in moves:
            dx, dy = move

            x = row + dx
            y = col + dy

            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] % 2 == 1:
                result += 1

        return result


# 0 -> 2 (Will be 1)
# 1 -> 3 (Will be 0)

"""
I think this question is quite easy.

The first thing I need to do is create a function to count live neighbors. When it comes to updating the 
current state based on the count of live neighbors, there are two approaches. One approach is to create 
a separate array to keep track of the coordinates that need to be updated later without modifying the board 
right away. The other approach is to change 0 to 2 and 1 to 3, allowing me to use the % operator to treat 
2 as 0 and 3 as 1 (using board[i][j] % 2 == 0 or board[i][j] % 2 == 1). I think the second method is better 
because it requires less space, so I chose it.
"""
