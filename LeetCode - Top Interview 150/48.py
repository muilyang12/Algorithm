# 48. Rotate Image
# https://leetcode.com/problems/rotate-image/


class Solution:
    def rotate1(self, matrix: List[List[int]]) -> None:
        numRowsCols = len(matrix)

        numbers = []

        top, bottom, left, right = 0, numRowsCols - 1, 0, numRowsCols - 1
        while len(numbers) < numRowsCols**2:
            for i in range(left, right + 1):
                numbers.append(matrix[top][i])
            top += 1

            if len(numbers) >= numRowsCols**2:
                break

            for i in range(top, bottom + 1):
                numbers.append(matrix[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                numbers.append(matrix[bottom][i])
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                numbers.append(matrix[i][left])
            left += 1

            if len(numbers) >= numRowsCols**2:
                break

        top, bottom, left, right = 0, numRowsCols - 1, 0, numRowsCols - 1
        while len(numbers) > 0:
            for i in range(top, bottom + 1):
                matrix[i][right] = numbers.pop(0)
            right -= 1

            for i in range(right, left - 1, -1):
                matrix[bottom][i] = numbers.pop(0)
            bottom -= 1

            for i in range(bottom, top - 1, -1):
                matrix[i][left] = numbers.pop(0)
            left += 1

            for i in range(left, right + 1):
                matrix[top][i] = numbers.pop(0)
            top += 1
