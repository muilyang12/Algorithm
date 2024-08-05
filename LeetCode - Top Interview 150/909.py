# 909. Snakes and Ladders
# https://leetcode.com/problems/snakes-and-ladders/


from typing import List


class Solution:
    def __init__(self):
        self.size = None

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        self.size = len(board)

        history = []
        result = []

        queue = [(1, 0)]

        while queue:
            current, current_movement = queue.pop(0)

            history.append(current)

            for i in range(6):
                if current + i == self.size**2:
                    result.append(current_movement + (0 if i == 0 else 1))

                    break

                next_x, next_y = self.get_coordinate(current + i)

                if board[next_x][next_y] != -1:
                    if board[next_x][next_y] in history:
                        continue

                    queue.append((board[next_x][next_y], current_movement + 1))
                    print(current + i, queue)

        return min(result)

    def get_coordinate(self, number: int):
        temp_number = number - 1

        quotient = temp_number // self.size
        remainder = temp_number % self.size

        row = self.size - 1 - quotient
        col = remainder if quotient % 2 == 0 else self.size - 1 - remainder

        return (row, col)


solution = Solution()
print(solution.snakesAndLadders([[-1, -1, -1], [-1, 9, 8], [-1, 8, 9]]) == 1)
print(solution.snakesAndLadders([[1, 1, -1], [1, 1, 1], [-1, 1, 1]]) == -1)
print(
    solution.snakesAndLadders(
        [[-1, 1, 2, -1], [2, 13, 15, -1], [-1, 10, -1, -1], [-1, 6, 2, 8]]
    )
    == 2
)
