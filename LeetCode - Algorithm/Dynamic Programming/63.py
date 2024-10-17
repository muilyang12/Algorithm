# 63. Unique Paths II
# https://leetcode.com/problems/unique-paths-ii/

from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numRows = len(obstacleGrid)
        numCols = len(obstacleGrid[0])

        possibleNumPathes = [[0 for __ in range(numCols)] for _ in range(numRows)]

        for i in range(numRows):
            if obstacleGrid[i][0] == 1:
                break

            possibleNumPathes[i][0] = 1
        for j in range(numCols):
            if obstacleGrid[0][j] == 1:
                break

            possibleNumPathes[0][j] = 1

        for i in range(1, numRows):
            for j in range(1, numCols):
                if obstacleGrid[i][j] == 1:
                    continue

                possibleNumPathes[i][j] = (
                    possibleNumPathes[i - 1][j] + possibleNumPathes[i][j - 1]
                )

        return possibleNumPathes[-1][-1]
