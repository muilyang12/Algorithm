# 120. Triangle
# https://leetcode.com/problems/triangle/

from typing import List
import math


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        memo = [[triangle[0][0]]]

        for i in range(1, len(triangle)):
            memo.append([])

            for j in range(len(triangle[i])):
                memoValue = triangle[i][j]
                upperLayer = math.inf
                if j - 1 >= 0:
                    upperLayer = min(upperLayer, memo[i - 1][j - 1])

                if j < len(memo[i - 1]):
                    upperLayer = min(upperLayer, memo[i - 1][j])

                memo[i].append(memoValue + upperLayer)

        return min(memo[-1])
