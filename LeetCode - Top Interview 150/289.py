from typing import List


class Solution:
    def count_live_neighbors(self, board: List[List[int]], row: int, col: int):
        xMax = len(board)
        yMax = len(board[0])
        dxdy = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

        count = 0

        for dx, dy in dxdy:
            x = row + dx
            y = col + dy

            if x < 0 or x >= xMax:
                continue
            if y < 0 or y >= yMax:
                continue

            if board[x][y] == 1:
                count += 1

        return count

    def gameOfLife(self, board: List[List[int]]) -> None:
        copied_board = [row[:] for row in board]
        xMax = len(board)
        yMax = len(board[0])

        for x in range(xMax):
            for y in range(yMax):
                count = self.count_live_neighbors(copied_board, x, y)

                if copied_board[x][y] == 1 and count < 2:
                    board[x][y] = 0

                elif copied_board[x][y] == 1 and count > 3:
                    board[x][y] = 0

                elif copied_board[x][y] == 0 and count == 3:
                    board[x][y] = 1


solution = Solution()
solution.gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]])
solution.gameOfLife([[1, 1], [1, 0]])
