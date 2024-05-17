# 54. Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
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
