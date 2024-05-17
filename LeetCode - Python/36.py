# 36. Valid Sudoku
# https://leetcode.com/problems/valid-sudoku


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        boardSize = 9

        print(boardSize)

        for i in range(boardSize):
            usedNumbers = []
            for j in range(boardSize):
                value = board[i][j]

                if value == ".":
                    continue

                if value in usedNumbers:
                    return False
                else:
                    usedNumbers.append(value)

            usedNumbers = []
            for j in range(boardSize):
                value = board[j][i]

                if value == ".":
                    continue

                if value in usedNumbers:
                    return False
                else:
                    usedNumbers.append(value)

        for i in range((boardSize // 3) ** 2):
            usedNumbers = []

            quotient = i // 3
            remainder = i % 3

            for i in range(boardSize // 3):
                for j in range(boardSize // 3):
                    value = board[quotient * 3 + i][remainder * 3 + j]

                    if value == ".":
                        continue

                    if value in usedNumbers:
                        return False
                    else:
                        usedNumbers.append(value)

        return True
