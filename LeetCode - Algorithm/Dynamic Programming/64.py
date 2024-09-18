# 64. Minimum Path Sum
# https://leetcode.com/problems/minimum-path-sum/

from typing import List
import math


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rowCount = len(grid)
        colCount = len(grid[0])

        memo = [[num for num in grid[i]] for i in range(rowCount)]

        for i in range(rowCount):
            for j in range(colCount):
                oneStepBefore = math.inf

                if j - 1 >= 0:
                    oneStepBefore = min(oneStepBefore, memo[i][j - 1])
                if i - 1 >= 0:
                    oneStepBefore = min(oneStepBefore, memo[i - 1][j])

                memo[i][j] += oneStepBefore if oneStepBefore != math.inf else 0

        return memo[-1][-1]
