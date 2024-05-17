# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        copiedMatrix = [row[:] for row in matrix]

        result = []
        while True:
            targets = copiedMatrix.pop(0)
            for target in targets:
                result.append(target)

            if len(copiedMatrix) == 0 or len(copiedMatrix[0]) == 0:
                break

            for i in range(len(copiedMatrix)):
                target = copiedMatrix[i].pop()
                result.append(target)

            if len(copiedMatrix) == 0 or len(copiedMatrix[0]) == 0:
                break

            targets = copiedMatrix.pop()
            for target in reversed(targets):
                result.append(target)

            if len(copiedMatrix) == 0 or len(copiedMatrix[0]) == 0:
                break

            for i in range(len(copiedMatrix) - 1, -1, -1):
                target = copiedMatrix[i].pop(0)
                result.append(target)

            if len(copiedMatrix) == 0 or len(copiedMatrix[0]) == 0:
                break

        return result

    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        result = []

        if not matrix:
            return result

        numRows, numCols = len(matrix), len(matrix[0])
        top, bottom, left, right = 0, numRows - 1, 0, numCols - 1

        while True:
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            if len(result) >= numRows * numCols:
                break

            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            if len(result) >= numRows * numCols:
                break

            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

            if len(result) >= numRows * numCols:
                break

            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

            if len(result) >= numRows * numCols:
                break

        return result
