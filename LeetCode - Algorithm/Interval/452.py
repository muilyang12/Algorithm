# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points = sorted(points, key=lambda x: x[0])

        result = 0

        narrowTarget = points[0]
        right = 1

        while right <= len(points):
            if right == len(points):
                result += 1

                break

            if narrowTarget[1] >= points[right][0]:
                narrowTarget[0] = max(narrowTarget[0], points[right][0])
                narrowTarget[1] = min(narrowTarget[1], points[right][1])
                right += 1
            else:
                result += 1

                narrowTarget = points[right]
                right += 1

        return result


"""
[[1,6],[2,8],[7,12],[10,16]]
   ^     ^

[[1,2],[2,3],[3,4],[4,5]]
   ^     ^

[[0,9],[0,6],[2,9],[2,8],[3,9],[3,8],[3,9],[6,8],[7,12],[9,10]]
   ^     ^
"""
