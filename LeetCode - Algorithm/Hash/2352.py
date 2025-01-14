# 2352. Equal Row and Column Pairs
# https://leetcode.com/problems/equal-row-and-column-pairs/

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        result = 0

        memory = {}

        for row in grid:
            rowTuple = tuple(row)

            if rowTuple in memory:
                memory[rowTuple] += 1
            else:
                memory[rowTuple] = 1

        for i in range(len(grid)):
            col = []

            for j in range(len(grid)):
                col.append(grid[j][i])

            colTuple = tuple(col)

            if colTuple in memory:
                result += memory[colTuple]

        return result
