# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

from typing import List
from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        numRows = len(grid)
        numCols = len(grid[0])

        result = 0

        for i in range(numRows):
            for j in range(numCols):
                if grid[i][j] == "1":
                    self.bfsFill(grid, i, j)
                    result += 1

        return result

    def bfsFill(self, grid, startX, startY):
        numRows = len(grid)
        numCols = len(grid[0])

        queue = deque()

        queue.append((startX, startY))

        while queue:
            x, y = queue.popleft()

            dxdys = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            for dx, dy in dxdys:
                if x + dx < 0 or x + dx >= numRows:
                    continue

                if y + dy < 0 or y + dy >= numCols:
                    continue

                if grid[x + dx][y + dy] == "1":
                    grid[x + dx][y + dy] = "2"
                    queue.append((x + dx, y + dy))
