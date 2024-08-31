# 547. Number of Provinces
# https://leetcode.com/problems/number-of-provinces/

from typing import List


class Solution:
    # time complexity: O(n^2)
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)

        result = 0

        visitedNodes = set()

        for i in range(n):
            if not i in visitedNodes:
                self.dfsSearch(isConnected, i, visitedNodes)
                result += 1

        return result

    def dfsSearch(
        self, isConnected: List[List[int]], nodeNum: int, visitedNodes: set[int]
    ):
        n = len(isConnected)

        for j in range(n):
            if j in visitedNodes or j == nodeNum:
                continue

            if isConnected[nodeNum][j] == 1:
                visitedNodes.add(j)
                self.dfsSearch(isConnected, j, visitedNodes)
